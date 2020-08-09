#!/usr/bin/python3.8
# coding:u8


from text_to_speech import say_text
from speech_rec import listen_text


def main_loop():
    quitter = False

    while not quitter :
        # repeate a sentence.
        text = listen_text()
        say_text(text)
        
        if "quitter" in text :
            quitter = True
            say_text("A bientôt.")


if __name__ == '__main__':
    main_loop()




# cd /home/jaenne/Python/talk_with_a_bot
# ./talking_bot.py