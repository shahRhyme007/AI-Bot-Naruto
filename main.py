import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import subprocess, sys
import random
import pygame
import datetime
from mykey import apiKey
import openai


chatbyNaruto = ""

def chat(query): 
    global chatbyNaruto
    print(chatbyNaruto)
    openai.api_key = apiKey
    chatbyNaruto += f"Rhyme: {query}\n Naruto: "
    

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = chatbyNaruto , 
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # wrap this inside a try-catch
    say(response["choices"][0]["text"])
    chatbyNaruto += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]



def ai(prompt):
    openai.api_key = apiKey
    text = f"OpenAI response for prompt: {prompt} \n *************************************************\n\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = prompt, 
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # wrap this inside a try-catch
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]

    if not os.path.exists("Openai"): 
        os.mkdir("Openai")
    
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f: 
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone()  as source: 
        r.pause_threshold = 1
        audio = r.listen(source)
        try: 
            query = r. recognize_google(audio, language="en-BD" )
            print(f"User said: {query}")
            return query
        except Exception as e: 
            return ""

if __name__ == '__main__':
    print("PyCharm")
    say("Hello, I am Naru tow")
    while (True):
        print("Listening...")
        query = takeCommand()

        # todo: add more websitess
        # for opening websites
        sites = [["youtube", "https://www.youtube.com/"], ["wikipedia", "https://www.wikipedia.com/"], 
                ["google", "https://www.google.com/"],["instagram", "https://www.instagram.com/"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} my boss , Rhyme")
                webbrowser.open(site[1])
        

           
        # dictionary for my local apps
        apps = [["outlook","/Users/shahr/OneDrive/Desktop/Outlook.lnk"], ["discord", "/Users/shahr/OneDrive/Desktop/Discord.lnk"], 
                ["spotify", "/Users/shahr/OneDrive/Desktop/Spotify.lnk"],["instagram", "https://www.instagram.com/"], ]
        
        # for opening local apps
        for app in apps: 
            if f"open {app[0]}".lower() in query.lower(): 
                say(f"opening {app[0]} my boss")
                os.system (app[1])
        
        # for opening music
        if "play music" in query: 
            musicPath = "/Users/shahr/Downloads/abc.mp3"
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(musicPath)
            pygame.mixer.music.play()
        
        # for stopping music
        elif "stop music" in query:
            pygame.mixer.music.stop()


        # for getting time 
        elif "the time" in query: 
            currentTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            say(f"The time is {currentTime} my boss")
      

        elif "using artificial intelligence".lower() in query.lower() :
            ai(prompt= query)
        
        elif "naruto stop".lower() in query.lower(): 
            exit()
        elif "start chat".lower() in query.lower(): 
            chatbyNaruto= ""
        else: 
            print("Chat started............")
            chat (query)

