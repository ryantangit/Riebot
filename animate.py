from replit import db
import random
import re
import numpy as np

#db[gif_size] must be manually set to 0 in console after every database wipe

class Animate:
  def __init__(self, seed = 69):
    self.seed = seed
    
  
  def randomizer(self): #Keeping track of gifs
    if db["gif_size"] > 0:
      temp = random.randint(0, db["gif_size"] - 1)
      return "[" + str(temp) + "] " + db[str(temp)]
    else:
      return "There are no gifs in the database, please add some."
  
  def delete(self, x):
    x = re.split("\s", x)[3]

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
      gif = re.split("\s", gif)[3]
    
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

  