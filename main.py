# importing the pyttsx library
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
# Initialize recognizer class (for recognizing the speech)
engine = pyttsx3.init()
r = sr.Recognizer()
init_rec = sr.Recognizer()
translator = Translator()
print("Let's speak!!")
with sr.Microphone() as source:
    audio_data = init_rec.record(source, duration=5)
    print("Recognizing your text.............")
    text = init_rec.recognize_google(audio_data)
    translation = translator.translate(text, src='en', dest='la')
    print(text)
    engine.say(translation.text)
    print(translation.text)
    engine.runAndWait()