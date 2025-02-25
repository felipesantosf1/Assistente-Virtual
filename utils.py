import pyttsx3
import datetime

voz = pyttsx3.init()

def speak(frase):
    voz.say(frase)
    voz.runAndWait()

def time_hour():
    agora = datetime.datetime.now()
    return agora