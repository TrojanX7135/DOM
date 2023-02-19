# Python program to translate
# speech to text and text to speech


import speech_recognition as ear
import pyttsx3

# Khởi tạo trình nhận dạng giọng nói
DOM_ear = ear.Recognizer()

with ear.Microphone() as mic:
	# Đọc dữ liệu âm thanh từ micrô mặc định
	print("I'm listening...")
	audio_data = DOM_ear.record(mic, duration=10)
	# Dịch ra văn bản
	# you = DOM_ear.recognize_google(audio_data)
	# print(you)
	try:
		you = DOM_ear.recognize_google(audio_data)
	except:
		you = "I can't hear"
	print(you)


