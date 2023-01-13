import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pywhatkit as kt


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        speak("Im listening to you now")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        speak("Recognayzing")
        text = recognizer.recognize_google(audio, language='en-in')
        speak(f"You said: {text}")

    except Exception as e:
        print(e)
        speak("Unable to Recognayze your voice.")
        return "None"
    return text


def functionality(text: str):
    my_web = webbrowser.get('chrome %s')

    if "google" in text:
        speak("What should i find?")
        find = take_command()
        kt.search(find)

    elif 'open youtube' in text:
        speak("Opening Youtube")
        my_web.open('youtube.com')

    elif 'open google' in text:
        speak("Opening Google")
        my_web.open('google.com')

    elif "open my projects" in text:
        speak("Opening your Git")
        my_web.open('github.com')

    elif "charm" in text:
        speak("Opening Pycharm")
        os.startfile(r"C:\Program Files\JetBrains\PyCharm 2022.1.1\bin\pycharm64.exe")

    else:
        speak("Probably i didnt get correctly")
        speak("Say again please")


if __name__ == '__main__':
    os.system('cls')
    wish_me()

    while True:
        start = input("\n 1 - Start\n 2 - Exit\n Your choice: ")
        if start == "1":
            query = take_command().lower()
            functionality(query)
        elif start == "2":
            speak("See ya later")
            exit(0)
        else:
            print("This variant does not exist!")
