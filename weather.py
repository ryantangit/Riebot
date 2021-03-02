import os
import requests
import json
from replit import db
import discord
from datetime import datetime


class Weather:
  def __init__(self, api_key):
    self.api_key = api_key
    self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
    self.weather_info = None

  def resolver(self, zipcode):
    
    if not zipcode:
      return "Please enter a valid zipcode"
    #Request using OpenWeatherMap API
    else:
        weather_req = requests.get(self.base_url + "appid="+ self.api_key+"&zip="+ zipcode[0])
        self.weather_info = weather_req.json()
        if(self.weather_info["cod"] == 200):
          return "Here is the weather!"
        else:
          return "Error Code " + str(self.weather_info["cod"]) + ": " + self.weather_info["message"]


  #CITY
  #Description
  #Temp:  / Feels_like:
  #Temp_min:   / Temp_max:
  #Humidity:   / Wind: m/second Direction
  def embed(self):
    
  ############  
  #HELPERS
    kToC = lambda kelvin: round(kelvin - 273.15, 1)
    kToF = lambda kelvin: round(kToC(kelvin) * 9/5, 1) + 32
    msTomph = lambda ms: round(ms * 2.237)
    def compass(degree):
      directions = [0, 45, 90, 135, 180, 225, 270, 315]
      direction_dict = {0: "N°", 45: "NE°", 90: "E°", 135: "SE°", 180:"S°", 225:"SW°", 270:"W°", 315:"NW°"}
      abs_dist = lambda list_degree: abs(degree - list_degree)
      closest = min(directions, key = abs_dist)
      return direction_dict[closest]
  ############    

    if(self.weather_info is not None and self.weather_info["cod"] == 200):
      #SETTING VARIABLES
      fTemp = str(kToF(self.weather_info["main"]["temp"]))+ "°F"
      cTemp = str(kToC(self.weather_info["main"]["temp"]))+ "°C"
      fTempFeels = str(kToF(self.weather_info["main"]["feels_like"]))+ "°F"
      cTempFeels = str(kToC(self.weather_info["main"]["feels_like"]))+ "°C"
      fTempMin = str(kToF(self.weather_info["main"]["temp_min"]))+ "°F"
      cTempMin = str(kToC(self.weather_info["main"]["temp_min"]))+ "°C"
      fTempMax = str(kToF(self.weather_info["main"]["temp_max"]))+ "°F"
      cTempMax = str(kToC(self.weather_info["main"]["temp_max"]))+ "°C"
      humidity = str(self.weather_info["main"]["humidity"])+ "% "+" "+" "+" "+" "
      windSpeed = str(msTomph(self.weather_info["wind"]["speed"])) + " mph"
      windDirection = compass(self.weather_info["wind"]["deg"])
      time_cur =  self.weather_info["dt"] + self.weather_info["timezone"]
      time_cur = datetime.utcfromtimestamp(time_cur).strftime('%m/%d %H:%M')



      #TITLE CREATION
      tit = self.weather_info["name"]+ ", " + self.weather_info["weather"][0]['description'].title() + ", " + time_cur
      #DESCRIPTION CREATION
      desc = "`Temp_cur: `" + fTemp + " / " + cTemp + "   " + "`Feels_like: `" + fTempFeels + " / " + cTempFeels +"\n`Temp_min: `" + fTempMin + " / " + cTempMin + "    " +"`Temp_Max: `" + fTempMax + " / " + cTempMax + "\n`Humidity: `" + humidity + "         " + "`Wind: `" + windSpeed + " " +  windDirection
      


      e = discord.Embed(title= tit, description= desc)
      e.set_image(url="http://openweathermap.org/img/wn/"+self.weather_info['weather'][0]['icon'] +"@2x.png")
      return [True, e]
    else:
      return [False, None]

