
from gtts import gTTS
tts = gTTS('hallo. Saya asisten suara anda,ada yang bisa dibantu', lang='id')
tts.save('Hallo.mp3')

from playsound import playsound
playsound('Hallo.mp3')

