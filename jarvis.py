import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Set up speech_recognition
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set up wake-up keyword
wake_word = "Jarvis"

# Define function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# Define function for opening a website
def open_website(url):
    webbrowser.open(url)
    speak("Opening website.")
    
# Define function for telling the time
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")
    
# Check if wake-up keyword is detected and listen for further commands
def listen_for_commands():
    with sr.Microphone() as source:
        print("Listening for the wake word...")
        r.adjust_for_ambient_noise(source)
        audio_wake_word = r.listen(source)
        
    
    try:
        # Check if wake-up word is mentioned
        if wake_word.lower() in r.recognize_google(audio_wake_word).lower():
            speak("Yes sir?")
            with sr.Microphone() as source:
                print("Listening for your command...")
                r.adjust_for_ambient_noise(source)
                audio_command = r.listen(source)
    
    
        # Convert speech to text
        command = r.recognize_google(audio_command)
        print("You said: " + command)
        
        # Execute command
        if "open" in command and "website" in command:
                words = command.split()
                url = None
                domain_extensions = ['.com', '.org', '.net', '.edu']
                
                for word in words:
                    if any(ext in word for ext in domain_extensions):
                        url = word
                        if not url.startswith("http"):
                            url = "http://" + url
                        break
                
                if url:
                    open_website(url)
                else:
                    speak("I'm not sure what you want me to open.")
        elif "time" in command:
                tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")
            
    except sr.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except sr.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet connection.")
while True:
    listen_for_commands()
