print("speak")

import pyttsx3

hHThuong_brain = "i'm just test this"

hHThuong_mouth = pyttsx3.init()
hHThuong_mouth.say(speak_content)
hHThuong_mouth.runAndWait()