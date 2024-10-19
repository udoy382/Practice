import pyttsx3
import speech_recognition as sr
import datetime
import pyowm
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition
r = sr.Recognizer()

# Initialize OpenWeatherMap API
owm = pyowm.OWM('YOUR_API_KEY')

# Greetings
greetings = ['Hello!', 'Hi!', 'Greetings!', 'Nice to see you!']


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print("Sorry, I couldn't request results. Check your internet connection.")
    return ""


def open_program(program_name):
    # Add code to open the program here
    speak(f"Opening {program_name}")


def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def get_weather(city):
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')["temp"]
    weather_status = w.get_status()
    speak(
        f"The weather in {city} is {weather_status}. The temperature is {temperature} degrees Celsius.")


def play_music():
    # Add code to play music here
    speak("Enjoy the music!")


def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a fish wearing a crown? King mackerel!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a bear with no teeth? A gummy bear!",
        "What do you call a fake noodle? An impasta!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't oysters donate to charity? Because they are shellfish!"
    ]
    joke = random.choice(jokes)
    speak(joke)


def jarvis():
    speak(random.choice(greetings))
    while True:
        text = get_audio()

        if "open" in text:
            program_name = text.split("open ")[-1]
            open_program(program_name)

        elif "time" in text:
            get_current_time()

        elif "weather" in text:
            city = text.split("weather in ")[-1]
            get_weather(city)

        elif "music" in text:
            play_music()

        elif "joke" in text:
            tell_joke()

        elif "how are you" in text or "what's up" in text:
            responses = ["I'm doing great, thank you!",
                         "I'm here to assist you!", "I'm functioning at optimal levels!"]
            speak(random.choice(responses))

        elif "your name" in text:
            speak("I am Jarvis, Your virtual assistant.")
