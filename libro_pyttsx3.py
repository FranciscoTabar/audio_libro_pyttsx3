import pyttsx3

# Configura el motor de texto a voz
engine = pyttsx3.init()

# Configura la voz (puedes ajustar el índice según las voces disponibles)
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"indice{i}:{voice.name}")
voice_index = 0
engine.setProperty('voice', voices[voice_index].id)  # Cambia el índice para seleccionar una voz diferente

# Lee el texto y reproduce el audio
archivo = open("app_libro/Include/libro.txt", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()

engine.say(texto)
engine.save_to_file(texto, 'audio-libro2.mp3')

# Cierra el motor de texto a voz
engine.runAndWait()