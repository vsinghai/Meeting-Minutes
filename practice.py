import speech_recognition as sr 
r = sr.Recognizer()

with sr.Microphone() as source: 
    print("Say something: ")
    audio = r.listen(source)

try:
    print('Google thinks you have said this:\n' + r.recognize_google(audio))
except:
    pass 

