import requests
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
          return "Error Code " + str(self.weather_info["cod"]) + ": " + self.weather_info["message"].title()



  #CITY, Description, Time
  #Temp: 
  #Feels_like:
  #Wind: 
  #Humidity:  
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
      # fTempMin = str(kToF(self.weather_info["main"]["temp_min"]))+ "°F"
      # cTempMin = str(kToC(self.weather_info["main"]["temp_min"]))+ "°C"
      # fTempMax = str(kToF(self.weather_info["main"]["temp_max"]))+ "°F"
      # cTempMax = str(kToC(self.weather_info["main"]["temp_max"]))+ "°C"
      humidity = str(self.weather_info["main"]["humidity"])+ "% "+" "+" "+" "+" "
      windSpeed = str(msTomph(self.weather_info["wind"]["speed"])) + " mph"
      windDirection = compass(self.weather_info["wind"]["deg"])
      time_cur =  self.weather_info["dt"] + self.weather_info["timezone"]
      time_cur = datetime.utcfromtimestamp(time_cur).strftime('%m/%d %H:%M')
      sun_rise = self.weather_info["sys"]['sunrise'] + self.weather_info["timezone"]
      sun_rise = datetime.utcfromtimestamp(sun_rise).strftime('%H:%M')
      sun_set = self.weather_info["sys"]['sunset'] + self.weather_info["timezone"]
      sun_set = datetime.utcfromtimestamp(sun_set).strftime('%H:%M')

      #TITLE CREATION
      tit = self.weather_info["name"]+ ", " + self.weather_info["weather"][0]['description'].title() + ", " + time_cur
      #DESCRIPTION CREATION
      desc = "`Temp current:` " + fTemp + " / " + cTemp + " \n" + "`Feels like:` " + fTempFeels + " / " + cTempFeels +"\n" + "`Wind Speed:` " + windSpeed + " " +  windDirection+ "\n" + "`Humidity:` " + humidity + "\n" + "`Sunrise:` " + sun_rise + "\n" + '`Sunset:` ' + sun_set
      
      

      #The default icons are boring so we gotta spice things up.
      image_id = self.weather_info['weather'][0]['icon']
      icon_to_html = {"01d": None, "02d": None, "03d": None, "04d": None, "09d": None, "10d": None, "11d": None, "13d":None, "50d": None, "01n": None, "02n": None, "03n": None, "04n": None, "09n": None, "10n": None, "11n": None, "13n": None, "50n": None}

      e = discord.Embed(title= tit, description= desc, colour = discord.Colour.dark_gold())
      e.set_thumbnail(url= "http://openweathermap.org/img/wn/" + image_id + "@2x.png")
      return [True, e]
    else:
      return [False, None]

