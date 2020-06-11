import speech_recognition as sr
import webbrowser
print("start talking")
r = sr.Recognizer()
with sr.Microphone() as source:
    audio=r.listen(source)
try:
    print("your text :"+r.recognize_google(audio))
except Exception:
    print("something went wrong")
p = r.recognize_google(audio)
print (p)
new=2;
url="http://"+p+".com";
print (url)
webbrowser.open(url,new=new)