from replit import db
import random
import re

#db[gif_size] must be manually set to 0 in console after every database wipe

class Animate:
  def __init__(self, seed = 69):
    self.seed = seed
    
  # Resolver on how to handle ANIMATE request from main.py
  # CASE not message: !riebot animate - Message is NULL
  # CASE message[0].isnumeric(): !riebot animate 1 - Message is ['1']
  # CASE message[0] == "insert": !riebot animate insert <link> - Message is ['insert', <link>]
  # Case message[0] == "delete": !riebot animate delete <link> - Message is ['delete', (int) x] 

  # Case ERROR: If something goes wrong, ERROR
  def resolver(self, message):
    if not message:
      return self.randomizer()
    elif message[0].isnumeric():
      return self.selected(message[0])
    elif message[0] == "insert" and len(message)> 1:
      return self.insert(message[1])
    elif message[0] == "delete" and len(message)> 1:
      return self.delete(message[1])
    return "Animate Resolver Error"

  #Select a particular gif using the corresponding db number.
  def selected(self, x):
    if(int(x) < 0 or int(x) >= db["gif_size"]):
      return "That animate number is invalid. The gif does not exist yet"
    else:
      return "[" + str(x) + "] " + db[str(x)]

  #Randomly out put a message.
  def randomizer(self): #Keeping track of gifs
    if db["gif_size"] > 0:
      temp = random.randint(0, db["gif_size"] - 1)
      return "[" + str(temp) + "] " + db[str(temp)]
    else:
      return "There are no gifs in the database, please add some."
  
  def delete(self, x):
    #Check gif is in database
    if(int(x) < 0 or int(x) >= db["gif_size"]):
      return "Can't delete a nonexistent gif"

    #Shift gifs into hole
    for i in range(int(x), db["gif_size"] - 1):
      db[str(i)] = db[str(i+1)]
    del db[str(db["gif_size"] - 1)]
    db["gif_size"] = db["gif_size"] - 1
    
    return "Gif [" + x + "] deleted!"

  def insert(self, gif):
    if (db["gif_size"] < 100):
      
      #Checking for duplicates.
      if(db["gif_size"] > 0):
        for i in range(0, db["gif_size"]):
          if(db[str(i)] == gif):
            return "This is a duplicate in the database! Use another one"
      #Make sure that the gif is from tenor and not some random link.
      if(gif.startswith("https://tenor.com/")):
        db[str(db["gif_size"])] = gif
        db["gif_size"] = db["gif_size"] + 1
        return "Insert of " + gif + " complete! [" + str(db["gif_size"] - 1) + "]"
      else:
        return "This gif is not from tenor.com"
    else:
      #If number of gifs has reached 100, we will figure it out later.
      return "We have reached maximum capacity on gifs"

  