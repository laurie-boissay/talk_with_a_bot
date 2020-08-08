#!/usr/bin/python3.8
# coding:u8


from text_to_speech import say_text
from speech_rec import listen_text


quitter = False

while not quitter :
	text = listen_text()
	say_text(text)
	print("Texte enregistré : ", text)
	if "quitter" in text :
		quitter = True
		say_text("A bientôt.")



# cd /home/jaenne/Python/talk_with_a_bot
# ./talking_bot.py