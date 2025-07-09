
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musicLibrary
import google.generativeai as genai

recognizer=sr.Recognizer()
engine= pyttsx3.init()
newsapi="key"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def aicommand(content):
    genai.configure(api_key="key") 
    model = genai.GenerativeModel("gemini-2.5-flash") 
    messages = [
        {"role": "user", "parts": "your are and desktop virtual assistant named jarvis, solving problem than alexa and google gemeni."},
        {"role": "model", "parts": "Understood. I am Jarvis, your desktop virtual assistant. How can I help you today?"}, # Jarvis's initial response
        {"role": "user", "parts": "content"}
        ]
    
    chat = model.start_chat(history=messages)
    response = chat.send_message(content)
    return response.text    

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com") 
    elif c.lower().startswith("play"):

        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link) 
    elif "news"in c.lower():
        r=requests.get("https://newsapi.org/v2/everything?q=Apple&from=2024-08-06&sortBy=popularity&apiKey={newsapi}")
        if r.status_code==200:
         data=r.json()
         articles=data.get('articles',[])
         for article in articles:
          speak(article['title']) 
    
    else:
        output=aicommand(c)
        speak(output)
                          



            
      

if __name__=="__main__":
    speak("Initializing Jarvis")
    while True:
        #listion  for wake word and obtain microphone audio
        r=sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone()as source:
                print("listening")
                audio=r.listen(source,timeout=3,phrase_time_limit=1)
            word=r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("ya") 
                #listen for word
                with sr.Microphone()as source:
                 print("jarvis activated")
                 audio=r.listen(source)
            command=r.recognize_google(audio)
            processCommand(command)

        except Exception as e:
            print("error,(0)",format(e))
        


   
