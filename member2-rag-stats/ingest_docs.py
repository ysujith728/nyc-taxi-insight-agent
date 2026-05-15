from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

# Folder containing PDFs
DOCS_PATH = "data/docs"

documents = []

# Load all PDF files
for file in os.listdir(DOCS_PATH):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(DOCS_PATH, file)

        loader = PyPDFLoader(pdf_path)
        docs = loader.load()

        documents.extend(docs)

print(f"Loaded {len(documents)} pages")

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS vector database
vectorstore = FAISS.from_documents(chunks, embeddings)

# Save locally
vectorstore.save_local("faiss_index")

print("FAISS index created successfully!")