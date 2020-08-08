#!/usr/bin/python3.8
# coding:u8

# RESSOURCES ______________________________________________________________________________
# https://pypi.org/project/SpeechRecognition/
# https://pythonprogramminglanguage.com/speech-recognition/
# https://stackoverflow.com/questions/62040401/alsa-error-running-a-flask-application-on-linux-ubuntu-using-pyaudio


import speech_recognition as sr
from text_to_speech import say_text


def listen_text():
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # listen for 1 second to calibrate the energy threshold for ambient noise levels.
        r.adjust_for_ambient_noise(source)
        print("Je vous écoute :")
        say_text("Je vous écoute.")
        audio = r.listen(source)

    try:
        text = "Vous avez dis :\n\n" + r.recognize_google(audio, language="fr-FR")
    except sr.UnknownValueError:
       text = "Je n'ai pas compris."
    except sr.RequestError as e:
       text = "Requête invalide : " + e

    print(text)
    return text