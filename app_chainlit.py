import time
inicio = time.time()

from create_functions import *
import chainlit as cl


##chainlit
@cl.on_chat_start
async def start():
    msg = cl.Message(content="Iniciando el bot...")
    await msg.send()
    
    retriever_model = load_model()    

    msg.content = "Ingrese su consulta"
    await msg.update()
    await msg.send()

    cl.user_session.set("retriever_model", retriever_model)

@cl.on_message
async def main(message: cl.Message):
    # Call the tool
    # tool()
    retriever_model = cl.user_session.get("retriever_model")
    
    # Send the final answer.
    await cl.Message(content=pregunta_clasificar(retriever_model, message.content)).send()

# end = time.time()
# print("------------------------------------")
# print(f"Tiempo de ejecución: {end - inicio} segundos")
# print("------------------------------------")
#