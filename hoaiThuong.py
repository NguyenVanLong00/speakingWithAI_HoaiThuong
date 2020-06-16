import pyttsx3
import speech_recognition
from datetime import date
from datetime import datetime
while True:
	#start listening
	hHThuong_ear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print("Thuong : i'm Listening")
		audio = hHThuong_ear.listen(mic)
	print("...")
	try:
		your_command = hHThuong_ear.recognize_google(audio)
	except:
		your_command =""
	print("you: "+your_command)
	
	#
	if "bye" in your_command:
		break
	#understand
	if "today" in your_command:
		today = date.today()
		hht_thinking = today.strftime("%B %d, %Y")
	elif "time" in your_command:
		now = datetime.now()
		hht_thinking = now.strftime("%B %d %Y %H o'clock %M minutes %S seconds")
	else:
		hht_thinking = "i don't understand"

	#speaking

	hHThuong_brain = hht_thinking
	print(hht_thinking)
	hHThuong_mouth = pyttsx3.init()
	hHThuong_mouth.say(hht_thinking)
	hHThuong_mouth.runAndWait()
