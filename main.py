import discord
import os
from webserver import cheese
from animate import Animate
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

  #!RIEBOT ANIMATE INSERT
  if local_message.startswith("!riebot animate insert"):
    await message.channel.send(animate.insert(local_message))
  
  #!RIEBOT ANIMATE DELETE
  elif local_message.startswith("!riebot animate delete"):
    await message.channel.send(animate.delete(local_message))


  #This is the Text Interaction between the bot and people.
  elif local_message.startswith("!riebot"):
    riebot_commands = {
      "!riebot help": riebot_help_msg,
      "!riebot whotao" : "HUUUU TAOOOOOOOOOO",
      "!riebot test": emote,
      "!riebot animate": animate.randomizer(),
    }

    

    #if the message fetched from dictionary is not null or not a variation of !riebot help %, send the else string to discord.
    if (local_message in riebot_commands or local_message.startswith("!riebot help")):
      await message.channel.send(riebot_commands.get(local_message))
    else:
      await message.channel.send("Try using `!riebot help` for more commands.")

cheese()
client.run(os.getenv('TOKEN'))