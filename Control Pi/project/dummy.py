#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
import time
import os
from gtts import gTTS
global data

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
# Record Audio
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        data = r.recognize_google(audio)
 
	# Speech recognition using Google Speech Recognition
    try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
	    
    return data

def jarvis(data):

    if "how are you" in data:
        print "true"
        speak("I am fine")
         
    if "what time is it" in data:
        speak(ctime())


time.sleep(2)
#speak("Hi Sai, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
