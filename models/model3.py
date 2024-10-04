from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
# Función para crear el VectorStore (almacenamiento de vectores)
def crear_vectorstore(documentos):
    embeddings = OpenAIEmbeddings()  # Utilizamos OpenAI para generar los embeddings
    vectorstore = FAISS.from_documents(documentos, embeddings)
    return vectorstore

# Función que crea el RAG a través de LangChain
def crear_rag(vectorstore):
    # Definimos el modelo OpenAI y el RetrievalQA Chain
    llm = OpenAI(temperature=0)  # Para generar respuestas más deterministas
    chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=vectorstore.as_retriever())
    return chain