import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests


#recoganize what we speak
recognizer=sr.Recognizer()

#initialize pyttsx(text to speech)
engine = pyttsx3.init()

#news api
news="431fb2315460459eab48035eaf5e2acd"
#creating jarvis voice
def speak(text):
    engine.say(text)
    engine.runAndWait()


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opening google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("opening youtube")    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("opening facebook")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("opening linkedin") 
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("opening instagram")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 
    else:
        pass         


if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone(device_index=2) as source:                  
                r.adjust_for_ambient_noise(source)
                print("Listening")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
                print("Got audio!")            
                word= r.recognize_google(audio)
                print(f"{word}")
                if word.lower()=="jarvis":
                    speak("ya")
                    #listen for command
                    with sr.Microphone(device_index=2) as source:                  
                        r.adjust_for_ambient_noise(source)
                        print("Listening")
                        audio = r.listen(source,timeout=3,phrase_time_limit=5)
                        print("Got audio!")            
                        command= r.recognize_google(audio)

                        processcommand(command)
        except Exception as e:
            print(f"An error occurred {e}")

