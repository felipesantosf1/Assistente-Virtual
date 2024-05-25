import json
import pyttsx3
import webbrowser
from datetime import datetime

voz = pyttsx3.init()
agora = datetime.now()

def speak(frase):
    voz.say(frase)
    voz.runAndWait()

def Comandos(frase):
    with open("comandos.json", "r") as arquivo:
        dados = json.load(arquivo)
        comandos = dados["comandos"]
        for comando in comandos:
            if any(identificador in frase for identificador in comando["identificador"]):
                name = comando["name"]
                if name == "abrir":
                    for item in comando["itens"]:
                        for palavra_chave in item["palavra_chave"]:
                            if palavra_chave in frase:
                                if item.get("url"):
                                    webbrowser.open(item["url"])
                                    speak(item["speak"])
                elif name == "horario":
                    speak(f"São {agora.hour}, horas e {agora.minute} minutos")
                elif name == "data":
                    speak(f"Hoje é dia {agora.day} do {agora.month} de {agora.year}")