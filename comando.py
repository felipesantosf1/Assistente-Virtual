import json
import webbrowser
import subprocess
from utils import speak, time_hour
from modulos.calcula import Calculadora
from modulos.pesquisa import realizar_pesquisa
from modulos.criaçao import Create

agora = time_hour()

def carregar_comandos():
    with open("comandos.json", "r") as arquivo:
        dados = json.load(arquivo)
        comandos = dados["comandos"]
    return comandos

def Comandos(frase, comandos):
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
                            elif item.get("name_program"):
                                subprocess.Popen(item["name_program"])
                                speak(item["speak"])
                                pass
            elif name == "horario":
                speak(f"São {agora.hour}, horas e {agora.minute} minutos")
            elif name == "data":
                speak(f"Hoje é dia {agora.day} do {agora.month} de {agora.year}")
            elif name == "calculadora":
                speak(Calculadora(frase))
            elif name == "pesquisa":
                speak(realizar_pesquisa(frase))
                
            elif name == "criar":
                for item in comando["itens"]:
                    for palavra_chave in item["palavra_chave"]:
                        if palavra_chave in frase:
                            name = item["objeto"]
                            speak(Create(name))