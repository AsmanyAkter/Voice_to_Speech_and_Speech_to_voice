import speech_recognition as sr

r = sr.Recognizer()

filename="sp.wav"


with sr.AudioFile(filename) as source:
	data= r.record(source)
	text=r.recognize_google(data)
	print(text)