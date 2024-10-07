from utils.utils import cargar_documentos, ejecutar_query
from models.model3 import crear_vectorstore, crear_rag
from utils import config

# from langchain_community.llms import OpenAI

if __name__ == "__main__":
    # Cargar documentos desde una ruta de archivos (por ejemplo, un archivo .txt)
    ruta_archivos = config.SOURCE_PATH  # Cambia esto por la ruta de tus archivos
    documentos = cargar_documentos(ruta_archivos)

    # Crear el VectorStore
    vectorstore = crear_vectorstore(documentos)

    # Crear el RAG chain
    cadena_rag = crear_rag(vectorstore)

    # Consulta a través del main
    query = input("Introduce tu consulta: ")
    respuesta = ejecutar_query(query, cadena_rag)

    print("Respuesta generada:")
    print(respuesta)
