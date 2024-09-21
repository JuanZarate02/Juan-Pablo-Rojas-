import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit
from datetime import datetime

# Motor de texto a voz
motor = pyttsx3.init()
asistente_virtual = "tomas"

# wikipedia en español
wikipedia.set_lang("es")


# Función para decir
def decir(texto):
    motor.say(texto)
    motor.runAndWait()

# Función para convertir audio a texto
def escuchar():
    reconocedor = sr.Recognizer()
    
    with sr.Microphone() as fuente:
        print("Escuchando...")
        audio = reconocedor.listen(fuente)
        
        try:
            comando = reconocedor.recognize_google(audio, language="es-ES") 
            print(f"Usted dijo: {comando}")
            return comando.lower()
       
        except sr.UnknownValueError:
            decir("Lo siento, no entendí eso.")
            return ""
        
        except sr.RequestError:
            decir("No puedo conectar con el servicio de reconocimiento de voz.")
            return ""

# Obtener hora
def obtener_hora():
    hora_actual = datetime.now().strftime("%H:%M")
    decir(f"La hora es {hora_actual}")

# Buscar en Wikipedia
def buscar_wikipedia(consulta):
    respuesta = wikipedia.summary(consulta, sentences=2, auto_suggest=False)
    decir(f"segun san Wiki, {respuesta}")
    print(respuesta)

# Abrir Google
def abrir_google():
    webbrowser.open("https://www.google.com")
    decir("Abriendo Google.")

# Reproducir YouTube
def poner_video_youtube(titulo_video):
    pywhatkit.playonyt(titulo_video)
    decir(f"Reproduciendo {titulo_video} en YouTube.")

# Proceso de comandos
def leer_comando(comando):
    if asistente_virtual in comando:
        comando = comando.replace(asistente_virtual, "").strip()

        if "hora" in comando:
            obtener_hora()
        
        elif "consulta en wikipedia" in comando:
            consulta = comando.replace("consulta en wikipedia", "").strip()
            if consulta:
                buscar_wikipedia(consulta)
            else:
                decir("Por favor, di qué quieres buscar en Wikipedia.")
        
        elif "abre google" in comando:
            abrir_google()

        elif "coloca" in comando and "youtube" in comando:
            titulo_video = comando.replace("coloca", "").replace("en youtube", "").strip()
            if titulo_video:
                poner_video_youtube(titulo_video)
            else:
                decir("que quieres colocar en youtube.")

        else:
            decir("Lo siento, no puedo ayudarte.")
    
    else:
        decir("primero debes decir mi nombre.")

# Ejecutar asistente
if __name__ == "__main__":
    decir(f"Hola, soy {asistente_virtual}, tu gran amigo. ¿Que vamos a hacer hoy?")
    
    while True:
        comando = escuchar()
        if comando:
            leer_comando(comando)