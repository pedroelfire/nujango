import os
from dotenv import load_dotenv
import openai
import json
from  .models import *

load_dotenv()

api_key = os.getenv("API_KEY")
client = openai.OpenAI(api_key=api_key)
modelo= "gpt-4-turbo"

def transcribirAudio():
    audio_file = open("./speech.mp3", "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text")
    return transcription

def llamarFuncion(question, previous_messages):
    #transcription = transcribirAudio()
    
    messages = []
    messages.append({"role": "system", "content": "Escucha el usuario y elige la funcion correcta, eres un asistente virtual llamado jack, resuelves preguntas de fittnes, ya sea acerca de comidas o de ejercicios, ahora te voy a proporcionar los datos de los habitos alimenticios en formato JSON, tu trabajo es leerlos y tomar esa informacion en cuenta para tu respuesta, aunque puede que no sea totalmente necesaria, aqui la informacion:  "})
    messages.append({"role": "system", "content": f"Estos son los ultimos mensajes de la conversacion con el cliente: {previous_messages}"})
    messages.append({"role": "user", "content": question}) 
    chat_response = chat_completion_request(messages, tools=tools)
    try:
        assistant_message = chat_response.choices[0].message.tool_calls[0].function
    except:
        return chat_response.choices[0].message.content
        
    function_name = assistant_message.name
    params = json.loads(assistant_message.arguments)
    messages.append(assistant_message)
    
    if function_name == "imprimir_huevo":
        return imprimir_huevo()
    elif function_name == "dar_clima":
        return dar_clima(params["ciudad"])
    else:
        return(assistant_message)


def chat_completion_request(messages, tools=None, tool_choice=None, model=modelo):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e
    
def imprimir_huevo():
    return "Imprimi un huevito con jamon"

def dar_clima(ciudad):
    return f"El clima en {ciudad} es de 100000 grados selsois"


tools = [
    {
        "type": "function",
        "function": {
            "name": "imprimir_huevo",
            "description": "Hace huevito con jamon",
        }
    },     {
        "type": "function",
        "function": {
            "name": "dar_clima",
            "description": "Da el clima de una ciudad",
            "parameters": {
                "type": "object",
                "properties": {
                    "ciudad": {
                        "type": "string",
                        "description": "En la ciudad de hidalgo del parral, o cualquier ciudad del mundo",
                    }
                },
                "required": ["ciudad"],
            },
        }
    }]


