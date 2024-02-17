# from create_functions import *
import os
import PyPDF2
import shutil
import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import time


start = time.time()

def load_collection():

    carpeta_a_eliminar = 'chroma'
    try:
        # Eliminar la carpeta y su contenido
        shutil.rmtree(carpeta_a_eliminar)
        print(f"La carpeta '{carpeta_a_eliminar}' ha sido eliminada exitosamente.")
    except FileNotFoundError:
        print(f"La carpeta '{carpeta_a_eliminar}' no existe.")
    except OSError as e:
        print(f"No se pudo eliminar la carpeta '{carpeta_a_eliminar}': {e}")

    chroma_client = chromadb.PersistentClient()
    print('Cargando modelo de embeddings EN CREATE_DB...')

    embed_model = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name='sentence-transformers/paraphrase-multilingual-mpnet-base-v2',
        device='cpu',
        normalize_embeddings=True
    )

    collection = chroma_client.get_or_create_collection(name='rosario', embedding_function=embed_model)

    # Ruta a la carpeta con libros
    folder_path = 'docs'

    # Obtener la lista de archivos en la carpeta
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

    for book_path in files:
        print(f'Archivo: {book_path}')
        with open(book_path, 'rb') as book:
            documents=[]
            metadata=[]
            ids=[]
            lector = PyPDF2.PdfReader(book)
            for i in range(len(lector.pages)):
                page = lector.pages[i]
                text = page.extract_text()
                documents.append(text)
                metadata.append({'file_path': book_path, 'page_label': i})
                ids.append(f'{book_path}-{i}')
            if len(documents) > 150:
                for i in range(0, len(documents), 150):
                    collection.add(
                        documents=documents[i:i+150],
                        metadatas=metadata[i:i+150],
                        ids=ids[i:i+150]
                    )
            else:
                collection.add(
                    documents=documents,
                    metadatas=metadata,
                    ids=ids
                )

    return collection


# end = time.time()
# print(end - start)

# from langchain_community.embeddings import HuggingFaceEmbeddings
# from llama_index import VectorStoreIndex
# from llama_index.embeddings import LangchainEmbedding
# from llama_index import ServiceContext
# from llama_index.storage.storage_context import StorageContext
# from llama_index.vector_stores import ChromaVectorStore


# def load_model():

#     carpeta_a_eliminar = 'chroma'
#     try:
#         # Eliminar la carpeta y su contenido
#         shutil.rmtree(carpeta_a_eliminar)
#         print(f"La carpeta '{carpeta_a_eliminar}' ha sido eliminada exitosamente.")
#     except FileNotFoundError:
#         print(f"La carpeta '{carpeta_a_eliminar}' no existe.")
#     except OSError as e:
#         print(f"No se pudo eliminar la carpeta '{carpeta_a_eliminar}': {e}")

#     chroma_client = chromadb.PersistentClient()
#     print('Cargando modelo de embeddings EN CREATE_DB...')

#     embed_model = embedding_functions.SentenceTransformerEmbeddingFunction(
#         model_name='sentence-transformers/paraphrase-multilingual-mpnet-base-v2',
#         normalize_embeddings=True
#     )

#     collection = chroma_client.get_or_create_collection(name='rosario', embedding_function=embed_model)

#     # Ruta a la carpeta con libros
#     folder_path = 'docs'

#     # Obtener la lista de archivos en la carpeta
#     files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

#     for book_path in files:
#         print(f'Archivo: {book_path}')
#         with open(book_path, 'rb') as book:
#             documents=[]
#             metadata=[]
#             ids=[]
#             lector = PyPDF2.PdfReader(book)
#             for i in range(len(lector.pages)):
#                 page = lector.pages[i]
#                 text = page.extract_text()
#                 documents.append(text)
#                 metadata.append({'file_path': book_path, 'page_label': i})
#                 ids.append(f'{book_path}-{i}')
#             if len(documents) > 150:
#                 for i in range(0, len(documents), 150):
#                     collection.add(
#                         documents=documents[i:i+150],
#                         metadatas=metadata[i:i+150],
#                         ids=ids[i:i+150]
#                     )
#             else:
#                 collection.add(
#                     documents=documents,
#                     metadatas=metadata,
#                     ids=ids
#                 )

#     embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
#         model_name='sentence-transformers/paraphrase-multilingual-mpnet-base-v2',
#         model_kwargs={'device': 'cpu'},
#         encode_kwargs={'normalize_embeddings': True}
#     )
#     )
#     print('Indexando documentos...')
    
#     print(10101010101010101010101010101010101010101010101010)

#     # set up ChromaVectorStore and load in data
#     vector_store = ChromaVectorStore(chroma_collection=collection)
#     storage_context = StorageContext.from_defaults(vector_store=vector_store)
#     service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=None)
 
#     index = VectorStoreIndex.from_vector_store(
#         vector_store, storage_context=storage_context, service_context=service_context, show_progress=True
#     )
    
#     retriever = index.as_retriever(similarity_top_k=2)

#     return retriever



# print("RESPUESTA")
# a = get_answer(load_model(), "¿Cuál es la historia de Rosario?")
# print(a)
