import streamlit as st
import ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

st.title("Interactive Webpage Chat 🌐")
st.caption("Chat with a webpage using local AI models and RAG")

# Get the webpage URL from the user
user_webpage_url = st.text_input("Enter Webpage URL", type="default")

if user_webpage_url:
    # 1. Load the webpage data
    webpage_loader = WebBaseLoader(user_webpage_url)
    webpage_documents = webpage_loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    text_chunks = text_splitter.split_documents(webpage_documents)

    # 2. Initialize Ollama embeddings and vector store
    llama_embeddings = OllamaEmbeddings(model="llama3")
    vector_store = Chroma.from_documents(documents=text_chunks, embedding=llama_embeddings)

    # 3. Define Ollama Llama3 model interaction
    def interact_with_llama(question, context):
        formatted_prompt = f"Question: {question}\n\nContext: {context}"
        response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': formatted_prompt}])
        return response['message']['content']

    # 4. RAG Setup
    retriever = vector_store.as_retriever()

    def combine_documents(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def generate_response_with_rag(question):
        retrieved_docs = retriever.invoke(question)
        formatted_context = combine_documents(retrieved_docs)
        return interact_with_llama(question, formatted_context)

    st.success(f"Webpage {user_webpage_url} loaded successfully!")

    # Ask a question about the webpage
    user_question = st.text_input("Ask any question about the webpage")

    # Chat with the webpage
    if user_question:
        response_result = generate_response_with_rag(user_question)
        st.write(response_result)
