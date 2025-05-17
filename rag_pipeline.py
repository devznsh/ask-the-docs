from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from PyPDF2 import PdfReader

def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file format.")

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def get_llm():
    hf_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",  # ✅ Small and efficient
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
    )
    return HuggingFacePipeline(pipeline=hf_pipeline)

def answer_question_from_file(uploaded_file, question):
    text = extract_text_from_file(uploaded_file)
    if not text.strip():
        raise ValueError("The uploaded file is empty or unreadable.")

    chunks = chunk_text(text)
    if not chunks:
        raise ValueError("Failed to split the document into chunks.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embeddings)

    retriever = vectorstore.as_retriever()
    retrieved_docs = retriever.get_relevant_documents(question)
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    if not context:
        return "No relevant content found in the document."

    print("🔍 Retrieved Context:\n", context)

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        Use the following context to answer the question.
        
        Context:
        {context}

        Question: {question}

        Answer:
        """
    )

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template},
        return_source_documents=False
    )

    return qa_chain.run(question)
