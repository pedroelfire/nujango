import os
from dotenv import load_dotenv
import openai
import json

load_dotenv()

api_key = os.getenv("API_KEY")
client = openai.OpenAI(api_key=api_key)
modelo= "gpt-4-turbo"


def hacer_pregunta(pregunta):
    response = openai.ChatCompletion.create(
        model=modelo,
        messages=[
            {"role": "system", "content": "You are a fitness application user."},
            {"role": "user", "content": pregunta},
        ],
        api_key=api_key
    )

    return response.choices[0].message["content"]

def transcribirAudio():
    audio_file = open("./speech.mp3", "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text")
    return transcription

def llamarFuncion(transcription):
    print(transcription)
    messages = []
    messages.append({"role": "system", "content": "Escucha el usuario y elige la funcion correcta"})
    messages.append({"role": "user", "content": transcription})
    chat_response = chat_completion_request(messages, tools=tools)
    try:
        assistant_message = chat_response.choices[0].message.tool_calls[0].function
    except:
        print(chat_response.choices[0].message.content)
        return
    function_name = assistant_message.name
    params = json.loads(assistant_message.arguments)
    messages.append(assistant_message)
    print(assistant_message)
    
    if function_name == "imprimir_huevo":
        imprimir_huevo()
    elif function_name == "dar_clima":
        dar_clima(params["ciudad"])
    else:
        print("No se reconoció la función solicitada.")


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
    print("Imprimi un huevito con jamon")

def dar_clima(ciudad):
    print(f"El clima en {ciudad} es de 100000 grados selsois")


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
                        "description": "En la ciudad de hidalgo del parra, o cualquier ciudad del munedo",
                    }
                },
                "required": ["ciudad"],
            },
        }
    }]

llamarFuncion("Dame el clima en ")
