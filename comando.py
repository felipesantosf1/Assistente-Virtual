import json
import pyttsx3

voz = pyttsx3.init()

def speak(frase):
    voz.say(frase)

def Comandos(frase):
    with open("comandos.json", "r") as arquivo:
        dados = json.load(arquivo)
        comandos = dados["comandos"]