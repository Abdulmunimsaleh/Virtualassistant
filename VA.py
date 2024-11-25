import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import time

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Uncomment the line below if you want to use the second voice
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)  # Use second voice, you can change this

def speak(audio):
    """Function to convert text to speech"""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Function to wish based on the time of the day"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Smartboy")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Smartboy")
    else:
        speak("Good Evening Smartboy")
    speak("I am your Assistant Emma")

def takeCommand():
    """Function to take voice input from the microphone and convert to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        print(e)
        speak("Sorry Smartboy, can you repeat that again?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can I help you?")
        query = takeCommand().lower()

        # Skip processing if the command is invalid ("None")
        if query == "none" or query == "":
            continue  # Simply skip the loop if no valid query

        # Wikipedia search
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find any information on that.")

        # Opening websites
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("YouTube is now open.")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Google is now open.")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("Gmail is now open.")

         # Send email functionality
        elif 'send email' in query:  # Add command for sending an email
            speak("Who would you like to send the email to?")
            recipient = takeCommand().lower()  # Ask for the recipient's email address
            speak("What is the subject of the email?")
            subject = takeCommand().lower()  # Ask for the subject of the email
            speak("What would you like to say in the body of the email?")
            body = takeCommand().lower()  # Ask for the body content of the email
            
            # Construct the Gmail URL with the given recipient, subject, and body
            mail_to = recipient.replace(" ", "")  # Remove spaces in email address (if any)
            mail_subject = subject.replace(" ", "+")  # Replace spaces with '+' for the URL
            mail_body = body.replace(" ", "+")  # Replace spaces with '+' for the URL
            
            # Construct the URL to open the Gmail compose page with pre-filled values
            gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={mail_to}&su={mail_subject}&body={mail_body}"
            
            # Open Gmail in the browser and compose the email
            webbrowser.open(gmail_url)
            speak(f"Gmail is now open. Composing an email to {recipient} with the subject {subject}.")
        
        # Playing music
        elif 'play music' in query:
            try:
                music_dir = 'D:\\music'  # Update the path according to your system
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Music is being played.")
            except Exception as e:
                speak("Sorry, I couldn't play the music.")

        # Telling the time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}.")

        # Opening VS Code
        elif 'open code' in query:
            try:
                codepath = "C:\\Users\\Abdulmuniim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Update path
                os.startfile(codepath)
            except Exception as e:
                speak("Sorry, I couldn't open VS Code.")

        # Stopping the assistant
        elif 'stop' in query:
            speak("See you soon, Smartboy.")
            exit()

        # Handling general queries and opening them in the browser
        elif query and not query.isspace():
            try:
                speak(f"Searching for {query}")
                webbrowser.open(query)
                time.sleep(2)  # Optional: Delay before processing the next command
            except Exception as e:
                speak("I couldn't process your request. Please try again.")
        else:
            speak("I didn't understand that. Please try again.")
