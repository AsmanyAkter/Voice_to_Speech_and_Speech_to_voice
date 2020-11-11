from gtts import gTTS

import os

f=open('SpToText.txt')
x=f.read()

language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save("SpToText.wav")
os.system("SpToText.wav")