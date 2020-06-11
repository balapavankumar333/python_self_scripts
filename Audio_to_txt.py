import speech_recognition as sr
r=sr.Recognizer()
with sr.AudioFile ('govner.mp4') as source:
    audio= r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("working on...")
        print(text)
    except:
        print("sorry....try agin...")
    








