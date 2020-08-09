# RESSOURCES ______________________________________________________________________________
# https://pypi.org/project/SpeechRecognition/
# https://pythonprogramminglanguage.com/speech-recognition/
# https://stackoverflow.com/questions/62040401/alsa-error-running-a-flask-application-on-linux-ubuntu-using-pyaudio


import sys


import speech_recognition as sr
from text_to_speech import say_text


def listen_text():
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # listen for 1 second to calibrate the energy threshold for ambient noise levels.
        r.adjust_for_ambient_noise(source)
        sys.stdout.write("Je vous écoute.\n")
        say_text("Je vous écoute.")
        audio = r.listen(source)

    try:
        text = "Vous avez dit :\n" + r.recognize_google(audio, language="fr-FR") + "\n"
    except sr.UnknownValueError:
       text = "Je n'ai pas compris." + "\n"
    except sr.RequestError as e:
       text = "Requête invalide : " + e + "\n"

    sys.stdout.write(text)
    return text