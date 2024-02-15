from create_functions import *
import chainlit as cl
import pickle

clasificador = pickle.load(open('clasificador.pickle', 'rb'))
vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))

##chainlit
@cl.on_chat_start
async def start():
    msg = cl.Message(content="Iniciando el bot...")
    await msg.send()
    
    retriever_model = load_model()    
    
    await cl.sleep(4)
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
    # await cl.Message(content="This is the final answer").send()
    await cl.Message(content=get_answer(retriever_model, message.content)).send()
