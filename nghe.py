import speech_recognition # thư viện speech_recognition

trojan_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("I'm listening")
	audio = trojan_ear.listen(mic)

# dòng số 4 tương đương:
# mic = speech_recognition.Microphone
# khác biệt khi dùng with là kết thúc hàm with (kết thúc nghe dòng 6)
# mic sẽ tắt.

try:
you = trojan_ear.recognizer_google(audio)
except:
	you = "I can't hear"
	
print(you)
