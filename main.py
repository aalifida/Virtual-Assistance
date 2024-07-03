import speech_recognition as sr
import webbrowser as web
import pyttsx3 as ttx

# Initialize text-to-speech engine
engine = ttx.init()

def Speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        web.open("http://www.google.com")
        Speak("Opening Google")
    if "open linkedin" in c.lower():
        web.open("http://www.linkedin.com")
        Speak("Opening Linkedin")
    if "open facebook" in c.lower():
        web.open("http://www.facebook.com")
        Speak("Opening facebook")
    if "open youtube" in c.lower():
        web.open("http://www.youtube.com")
        Speak("Opening Youtube")

if __name__ == "__main__":
    print("Initializing Jarvis...")
    Speak("Initializing Jarvis")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for activation word 'Jarvis'...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(f"Recognized word: {word}")
            if "jarvis" in word.lower():
                print("Jarvis Initialized")
                Speak("Yes Sir")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    print(f"Recognized command: {command}")
                    if "shutdown" in command.lower():
                        break
                    else:
                        processCommand(command)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

