import speech_recognition as sr
import pyttsx3
from nltk.tokenize import word_tokenize
from comando import Comandos

microfone = sr.Recognizer()
voz = pyttsx3.init()

def Tratamento_frase(palavras):
    artigos = ["o","a","os","as"]
    palavras_filtradas = [palavra for palavra in palavras if palavra not in artigos]
    return " ".join(palavras_filtradas)

def speak(frase):
    voz.say(frase)
    voz.runAndWait()


def Iniciando_Assistente():
    print("Ouvindo...")
    while True:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source, None, 5)
            try:
                frase = microfone.recognize_google(audio, language="pt-br").lower()
                palavras = word_tokenize(frase)
                frase = Tratamento_frase(palavras)
                print(f"Usuario>>{frase}")
                Comandos(frase)
                if frase == "obrigado":
                    speak("De nada")
                    break
            except sr.UnknownValueError:
                print("Não consigo escutalo!")