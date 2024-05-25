import speech_recognition as sr
import pyttsx3
from back import Iniciando_Assistente

microfone = sr.Recognizer()
voz = pyttsx3.init()

def speak(frase):
    voz.say(frase)
    voz.runAndWait()


def Assistente():
    while True:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source, None, 5)
            try:
                frase = microfone.recognize_google(audio, language="pt-br").lower()
                print(f"Usuario>>{frase}")
                if "eva" in frase or "iniciar" in frase:
                    speak("Iniciando")
                    Iniciando_Assistente()
            except sr.UnknownValueError:
                print("Não consigo escutalo!")

Assistente()