""" 
ALLMIGHT - A Voice Assistant 
description: voice controlled AI assistant named "Allmight" that can perform various tasks 
             such as playing music, opening websitestand 
             user commands and text-tos, fetching news headlines, and interacting 
             with an AI model for conversational responses. It uses speech recognition to under-speech to respond.
"""

import os
import warnings
import speech_recognition as sr
import webbrowser
import music_library
import requests
import edge_tts
import asyncio
import pygame
import time
import whisper
from google import genai
from dotenv import load_dotenv

#________setup________

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
warnings.filterwarnings("ignore", category=UserWarning, module='pkg_resources')

load_dotenv()
pygame.mixer.init()

# api clients

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
newsapi = os.getenv("NEWS_API_KEY")
recognizer = sr.Recognizer()



def speak(text):
    # this func converts text to speech using edge-tts and plays the audio
   
    print(f"allmight: {text}")

    async def generate_audio():
        voices = ["en-US-GuyNeural", "en-GB-RyanNeural", "en-US-GuyNeural"]
        for voice in voices:
            try:
                communicate = edge_tts.Communicate(text, voice)
                await communicate.save("temp.mp3")
                return  
            except Exception:
                continue 

    asyncio.run(generate_audio())

    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


# AI function

def ask_ai(command):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"You are allmight, a helpful voice assistant. Answer in the same language as the user's question (Hindi, English, or Hinglish). Keep it short, natural, and conversational: {command}",
        )
        return response.text.replace("*", "")
    except Exception as e:
        print(f"DEBUG - AI Error: {e}")
        return "I am unable to connect to the brain module right now."


# --------------------------------------------------------------------
def process_command(c):
    # handles system commands and routes

    print(f"---> You said: {c}")
    cmd = c.lower()
    if "play" in cmd:
        song_found = None
        for song in music_library.music:
            if song in cmd:
                song_found = song
                break
        
        if song_found:
            speak(f"Playing {song_found} from your library.")
            webbrowser.open(music_library.music[song_found])
        else:
            import pywhatkit
            search_query = cmd.replace("play", "").replace("the", "").replace("can", "").replace("you", "").replace("song", "").strip()
            speak(f"Playing {search_query} from YouTube.")
            pywhatkit.playonyt(search_query)
        return

    elif "open google" in cmd:
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "close google" in cmd:
            speak("closing google")
            os.system("taskkill /f /im chrome.exe ") #this command will close all tabs of Google Chrome
            return

    elif "open youtube" in cmd:
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "close youtube" in cmd:
            speak("closing youtube")
            os.system("taskkill /f /im chrome.exe ")
            return

    elif "open linkedin" in cmd:
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif "close linkedin" in cmd:
            speak("closing linkedin")
            os.system("taskkill /f /im chrome.exe ")
            return

    elif "news" in cmd:
        speak("here are the top news headlines")
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        )
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles[:3]:
                headline = article["title"]
                print(f"DEBUG: reading headline: {headline}")
                speak(headline)

                time.sleep(1)
        return

    else:
        speak("let me think.....")
        ai_reply = ask_ai(c)
        speak(ai_reply)

    speak("Is there anything else I can assist you with?")


# -------------------------------------------------------------------------------

# main loop

if __name__ == "__main__":
    speak("System online.")
    while True:
        r = sr.Recognizer()
        r.pause_threshold = 1.0
        print("\n[Status: Recognizing...]")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("[Status: Listening...]")
                audio = r.listen(source, timeout=3, phrase_time_limit=5)

            word = r.recognize_whisper(audio, language="en")
            print(f"DEBUG: I heard: '{word}'")

            if "allmight" in word.lower().replace(" ", "") or "ok" in word.lower().replace(" ", ""):
                speak("Yes, sir?")
                time.sleep(1)

                active = True
                while active:
                    print("[Status: Listening for command...]")
                    with sr.Microphone() as source:
                        r.pause_threshold = 1.0
                        audio = r.listen(source, phrase_time_limit=8)
                        command = r.recognize_whisper(audio, language="en")

                        if "nothing" in command.lower() or "bye" in command.lower():
                            speak("Understood. Standing by.")
                            active = False
                        else:
                            process_command(command)
        except Exception:
            continue
