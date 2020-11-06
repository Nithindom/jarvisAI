import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
from twilio.rest import Client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Ver Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Ver Good Afternoon Sir!")
    else:
        speak("Ver Good Evening Sir!")

    speak(" I am Jarvis, A computer program designed by Mr.Nithin")


# .......... Taking Command from Mike .........
def takecommand():
    print("1")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        r.energy_threshold = 200
        r.adjust_for_ambient_noise = .5
        audio = r.listen(source)
        try:
            print("Recog..")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}")
        except Exception as e:
            speak("Please say that again")
            return "none"
        return query

   
    # return query
    

# #.................Send message to whatsapp function.......................
# from_whatsapp_number = 'whatsapp:+14155238886'
# To_number = 'whatsapp:+918309559630'
# def send_whatsapp_alert():
#     client = Client(username="ACe4ed5f0fda971dc2332d590bb1c0a9da",password="46bb20844e963ac97bb16018aa12651d")
#     client.messages.create(body = "Hi",from_ = from_whatsapp_number,to = To_number)

# ......................Main Function........................
if __name__ == "__main__":
    wishme()
    while True:
        takecommand()
