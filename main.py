import discord
import os
from webserver import cheese
from animate import Animate
from weather import Weather
import re

#############
# Ryan Tan, Timothy Wu
# Last edited: 03/1/21
#
################

#Load in the client from the discord api
client = discord.Client()
animate = Animate()

emote = "⣿⣯⣿⣟⣟⡼⣿⡼⡿⣷⣿⣿⣿⠽⡟⢋⣿⣿⠘⣼⣷⡟⠻⡿⣷⡼⣝⡿⡾⣿\n⣿⣿⣿⣿⢁⣵⡇⡟⠀⣿⣿⣿⠇⠀⡇⣴⣿⣿⣧⣿⣿⡇⠀⢣⣿⣷⣀⡏⢻⣿\n⣿⣿⠿⣿⣿⣿⠷⠁⠀⠛⠛⠋⠀⠂⠹⠿⠿⠿⠿⠿⠉⠁⠀⠘⠛⠛⠛⠃⢸⣯\n⣿⡇⠀⣄⣀⣀⣈⣁⠈⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠠⠎⠈⠀⣀⣁⣀⣀⡠⠈⠉\n⣿⣯⣽⡿⢟⡿⠿⠛⠛⠿⣶⣄⠀⠀⠀⠀⠀⠀⠈⢠⣴⣾⠛⠛⠿⠻⠛⠿⣷⣶\n⣿⣿⣿⠀⠀⠀⣿⡿⣶⣿⣫⠉⠀⠀⠀⠀⠀⠀⠀⠈⠰⣿⠿⠾⣿⡇⠀⠀⢺⣿\n⣿⣿⠻⡀⠀⠀⠙⠏⠒⡻⠃⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠐⡓⢚⠟⠁⠀⠀⡾⢫\n⣿⣿⠀⠀⡀⠀⠀⡈⣉⡀⡠⣐⣅⣽⣺⣿⣯⡡⣴⣴⣔⣠⣀⣀⡀⢀⡀⡀⠀⣸\n⣿⣿⣷⣿⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢾⣷⣿\n⣿⣿⣟⠫⡾⠟⠫⢾⠯⡻⢟⡽⢶⢿⣿⣿⡛⠕⠎⠻⠝⠪⢖⠝⠟⢫⠾⠜⢿⣿\n⣿⣿⣿⠉⠀⠀⠀⠀⠈⠀⠀⠀⠀⣰⣋⣀⣈⣢⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⢸⣿\n⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿\n⣿⣿⣿⣿⣦⡔⠀⠀⠀⠀⠀⠀⢻⣿⡿⣿⣿⢽⣿⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿\n⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠘⠛⢅⣙⣙⠿⠉⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣅⠀⠓⠀⠀⣀⣠⣴⣺⣿⣿⣿⣿⣿⣿⣿⣿\n"

riebot_help_msg = "`animate` - Send out a random gif from the collection\n`animate insert <tenor gif url>` - Inserts a gif into the database, do not mess up the url or else the world is goign to end.\n`test` - testing\n`whotao` - Whotao?"

#This is the response that the bot should have when it is ready/loaded.
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
#Check on the message and see how to process it.
async def on_message(message):
  local_message = message.content.lower()
  #If the message is from us, then we don't do anything.
  if message.author == client.user:
    return

  message_split = re.split("\s", local_message)
  embed_with_me = False
  embedded = None
  #This is the Text Interaction between the bot and people.
  # First detect if the first part of the message is !riebot, then 
  # look through the list of commands.
  #
  # EX. ['!riebot', "command", "msg[2]", "msg[3]"]
  #
  if message_split[0] == "!riebot":
    riebot_response = "Try using `!riebot help` for more commands."
    if len(message_split) > 1:
      if message_split[1] == "help":
        riebot_response = riebot_help_msg
      elif message_split[1] == "whotao":
        riebot_response = "HUUUU TAOOOOOOOOOO"
      elif message_split[1] == "test":
        riebot_response = emote
      elif message_split[1] == "animate":
        riebot_response = animate.resolver(message_split[2:])
      elif message_split[1] == "weather":
        weather_bot = Weather(os.getenv('OpenWeather_API'))
        riebot_response = weather_bot.resolver(message_split[2:])
        embed_with_me, embedded = weather_bot.embed()
        
    
    #yeet message
    if(not embed_with_me):
      await message.channel.send(riebot_response)
    else:
      await message.channel.send(embed = embedded)


cheese()
client.run(os.getenv('TOKEN'))