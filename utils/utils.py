
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Función para cargar documentos
def cargar_documentos(ruta_archivos):
    loader = TextLoader(ruta_archivos)
    documentos = loader.load()
    # Dividimos los documentos en fragmentos más pequeños
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs_procesados = text_splitter.split_documents(documentos)
    return docs_procesados


# Función principal para ejecutar la query y obtener la respuesta
def ejecutar_query(query, cadena_rag):
    respuesta = cadena_rag.run(query)
    return respuesta