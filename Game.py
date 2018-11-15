#!/usr/bin/env
import speech_recognition as sr
sr.__version__
from PIL import Image


fruits = ["μήλο", "πορτοκαλί", "μπανάνα", "μανταρίνι", "φράουλα", "πεπόνι", "καρπούζι", "ρόδι"]
img = ["apple.jpg", "orange.jpg", "banana.jpg", "madarin.jpg", "strawberry.jpg", "melon.jpg", "watermelon.jpg", "rodi.jpg"]
length = len(fruits)


r = sr.Recognizer()
r.energy_threshold = 6500
r.pause_threshold = 2


for i in range(0, length):
    with sr.Microphone() as source:
        print('Say Something')
        with Image.open(img[i]) as image:
            image.show()
        image.close()
        audio = r.listen(source)
        print('Done')

    try:
        text = r.recognize_google(audio, language = "el-GR")
        print(text)
        if(text == fruits[i]):
            print('Correct\n')
        else:
            print('Try Again\n')

    except Exception as e:
        print(e)


    
