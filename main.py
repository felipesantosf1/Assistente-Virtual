import speech_recognition as sr
from nltk.tokenize import word_tokenize
from comando import Comandos, carregar_comandos
from utils import speak, time_hour

def Time_day():
    time = time_hour()
    hora = time.hour
    if 5 <= hora < 11:
        info = "Bom dia"
    elif 11 <= hora < 17:
        info = "Boa tarde"
    elif 17 <= hora <= 23 or 0 <= hora < 5:
        info = "Boa Noite"
    return info

def Tratamento_frase(palavras):
    artigos = ["o","a","os","as"]
    palavras_filtradas = [palavra for palavra in palavras if palavra not in artigos]
    return " ".join(palavras_filtradas)

microfone = sr.Recognizer()

def Assistente(comandos):
    while True:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source, None, 5)
            try:
                frase = microfone.recognize_google(audio, language= 'pt-br').lower()
                if any(palavra in frase for palavra in ["eva", "iniciar"]):
                    print("Ouvindo...")
                    boas_vindas = Time_day()
                    speak(f"{boas_vindas}")

                    # ASSISTENTE INICIADA
                    assistente_ativa = True
                    while assistente_ativa:
                        with sr.Microphone() as source:
                            microfone.adjust_for_ambient_noise(source)
                            audio = microfone.listen(source, None, 8)
                            try:
                                frase = microfone.recognize_google(audio, language= 'pt-br').lower()
                                palavras = word_tokenize(frase)
                                frase = Tratamento_frase(palavras)

                                print(f"Usuario>> {frase}")

                                Comandos(frase, comandos)

                                if frase in ["obrigado", "desligar", "brigado"]:
                                    speak("De nada")
                                    assistente_ativa = False
                            except sr.UnknownValueError:
                                print("Não consigo escutá-lo!")
                            except Exception as e:
                                print(f"Erro: {e}")

            except sr.UnknownValueError:
                print("")
            except Exception as e:
                print(f"Erro: {e}")


if __name__ == "__main__":
    print('Diga "eva", "iniciar" para começar.')
    comandos = carregar_comandos()
    Assistente(comandos)