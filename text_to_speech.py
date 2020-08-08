#!/usr/bin/python3.8
# coding:u8


# RESSOURCES _________________________________________________________________________
# https://pypi.org/project/pyttsx3/
# https://sonsuzdesign.blog/2020/06/07/building-a-speech-translator-in-python/

import pyttsx3


def say_text(text):
    engine = pyttsx3.init()                     # object creation.

    # RATE _______________________________________________________________________________
    rate = engine.getProperty('rate')           # getting details of current speaking rate.                            # printing current voice rate.
    engine.setProperty('rate', 100)             # setting up new voice rate.

    # VOLUME ______________________________________________________________________________
    volume = engine.getProperty('volume')       # getting to know current volume level.
    engine.setProperty('volume',1.0)            # setting up volume level between 0 and 1.

    # VOICE _______________________________________________________________________________
    voices = engine.getProperty('voices')       # getting details of current voice.
    engine.setProperty('voice', voices[0].id)   # 1 for female, 0 for male.

    # LANGUAGE ____________________________________________________________________________
    fr_voice_id = "french"                      # No french female voice.
    engine.setProperty('voice', fr_voice_id)    # Changing language to french.

    # SAY TEXT ______________________________________________________________________________
    engine.say(text)


    engine.runAndWait()
    engine.stop()