import speech_recognition as sr
import pyttsx3

microfone = sr.Recognizer()
voz = pyttsx3.init()

def speak(frase):
    voz.say(frase)
    voz.runAndWait()


def Iniciando_Assistente():
    while True:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source, None, 5)
            try:
                frase = microfone.recognize_google(audio, language="pt-br")
                print(f"Usuario>>{frase.lower()}")
                if frase == "obrigado":
                    speak("De nada")
                    break
            except sr.UnknownValueError:
                print("Não consigo escutalo!")