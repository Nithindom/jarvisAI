import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<4:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis, A computer program designed by Mr.Tony Stark")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please..")
        return "none"
    return query

if __name__ == "__main__":
    wishme()
    # speak('Hello Mr.Tony Stark')
    takecommand()
