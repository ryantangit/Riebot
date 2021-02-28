from replit import db
import random
import re
import numpy as np

db["gif_size"] = 0

class Animate:
  def __init__(self, seed = 69):
    self.seed = seed
    
  
  def test(self):
    temp = random.randint(0, db["gif_size"])
    return db[str(temp)] 
  


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
        return "Insert of " + gif + " complete!"
      else:
        return "This gif is not from tenor.com"
    else:
      #If number of gifs has reached 100, we will figure it out later.
      return "We have reached maximum capacity on gifs"

  