
import speech_recognition

hHThuong_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Thuong : i'm Listening")
	audio = hHThuong_ear.listen(mic)
try:
	your_command = hHThuong_ear.recognize_google(audio)
except:
	your_command =""
print("you: "+your_command)