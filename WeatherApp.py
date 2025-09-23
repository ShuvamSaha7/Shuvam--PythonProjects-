import requests #requests library helps us send requests to websites or APIs and get data back

import json

import win32com.client as wincom

city = input("Enter the name of the city\n:")

url = (f"http://api.weatherapi.com/v1/current.json?key=a5514eaacc684782ac425514251608&q= {city} ")

#This line 5 builds the URL (web address) where we will ask for weather data.

#YOUR_API_KEY = your personal secret key from WeatherAPI


r = requests.get(url) #This sends a GET request to the API using the url
                      #requests.get(url) goes to that web address and asks:"Please give me the weather data".
                      #The API replies with data(in JSON format) and that whole reply is stored in r.

#print(r.text) #r.text gives the full response text from the API (usually JSON format,which looks like a dictionary but is actually just a string)

wdic = json.loads(r.text) #converts that JSON string into a python dictionary

w = wdic["current"] ["temp_c"] #wdic["current"] -> goes inside the current section 
                               #["temp_c"] -> gets the temperature in celsius

#looks inside JSON string that converted into python dict -> find current section->then  under current get the value of temp_c -> save it into w.

speaker = wincom.Dispatch("SAPI.SpVoice")

text = (f"The current weather in {city} is {w} degrees")

speaker.speak(text)



