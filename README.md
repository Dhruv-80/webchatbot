## 💻 Local Llama-3 with RAG

Welcome to our Streamlit application, designed to facilitate interactions with any webpage using local Llama-3 and Retrieval Augmented Generation (RAG). Our app operates exclusively on your device, offering a seamless experience without relying on an internet connection.

### Key Features
- Input the URL of any webpage.
- Pose questions about the webpage's content.
- Receive accurate responses leveraging RAG and the locally deployed Llama-3 model.

### Getting Started

1. Clone our GitHub repository:

```bash
git clone < clone link >
```

2. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

3. Obtain your API Key

- Sign up for an account with your preferred LLM provider (such as OpenAI) and obtain your API key.

4. Launch the Streamlit App:

```bash
streamlit run llama3_local_rag.py
```

### How It Works

- Our application loads webpage data using WebBaseLoader and segments it into manageable chunks with RecursiveCharacterTextSplitter.
- It establishes Ollama embeddings and a vector store using Chroma for efficient processing.
- The app initiates a RAG (Retrieval-Augmented Generation) chain, retrieving relevant documents based on user queries.
- The Llama-3 model is then invoked to generate responses using the retrieved context.
- Finally, the application presents the answers to user inquiries with precision and accuracy.