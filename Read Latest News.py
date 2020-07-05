#here frst we have to get an API KEY from newsapi.org  https://newsapi.org/s/india-news-api
# #using the following modules 
import json
import requests
from win32com.client import Dispatch

def speak(str):
    speaker_number = 1
    speak = Dispatch("SAPI.SpVoice")
    vcs = speak.GetVoices()
    #SVSFlag = 11
    #print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
    speak.Voice
    speak.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
    speak.Speak(str)

if __name__ == "__main__":
    speak("Hello Sir, i'am Julia, your virtual assistant")
    speak("Top headlines from Indian News Sources today, Let's begin")
    url='http://newsapi.org/v2/top-headlines?country=in&apiKey=92e405b11c1d4002b3714bd7539fbc05'
    news=requests.get(url).text
    news_dict=json.loads(news)           #parsed a string with json
    #print(news_dict["articles"])
    
    arts=news_dict["articles"]
    for article in arts:
        speak(article["title"])
        speak("Now, moving on to the next news")
