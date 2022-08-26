# Import the required module for text 
# to speech conversion

from gtts import gTTS
import os

# The text that you want to convert to audio
file=open("texttospeech.txt")

x=file.read()

language='en'

welcome=gTTS(text=x,slow=False)

# Saving the converted audio in a mp3 file named
welcome.save("text_to_speech.wav")

os.system("text_to_speech.wav")