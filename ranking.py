from replit import db
import random
import discord
import datetime

#Set cooldown for exp in minutes (0-59)
COOLDOWN_MINUTE = 1 

class Ranking:
  def __init__(self, seed = 420):
    self.seed = seed

  #Give user a random amount of exp (1-50)
  def exp_gift(self, name):
    db[name + "_exp"] = db[name + "_exp"] + random.randint(1, 50)

  #Print out a user's current exp
  def status(self, name, avatar, display_name):
    message = "EXP: " + str(db[name + "_exp"])
    e = discord.Embed(title= display_name, description= message, colour = discord.Color.random())
    e.set_thumbnail(url= avatar)
    return [True, e]
  
  #Limit user's ability to earn exp to COOLDOWN_MINUTE
  def timer(self, name):
      #Check if user is already in database. If not, create new entry.
    db_keys = db.keys()
    if (name + "_exp") not in db_keys:
      db[name + "_exp"] = 0
      self.exp_gift(name)
      temp = datetime.datetime.now()
      db[name + "_time"] = [int(temp.strftime("%Y")), int(temp.strftime("%m")), int(temp.strftime("%d")), int(temp.strftime("%H")), int(temp.strftime("%M"))]
    #User exists. Check if user elgible for more exp.
    else:
      prev_exp = db[name + "_time"]
      temp = datetime.datetime.now()
      x = [int(temp.strftime("%Y")), int(temp.strftime("%m")), int(temp.strftime("%d")), int(temp.strftime("%H")), int(temp.strftime("%M"))]
      db[name + "_time"] = x
      #[year %Y, month %m, day $d, hour %H, minute %M]
      if(x[0] > prev_exp[0]):
        self.exp_gift(name)
      elif(x[1] > prev_exp[1]):
        self.exp_gift(name)
      elif(x[2] > prev_exp[2]):
        self.exp_gift(name)
      elif(x[3] > prev_exp[3]):
        self.exp_gift(name)
      elif(x[4] - prev_exp[4] >= COOLDOWN_MINUTE):
        self.exp_gift(name)
    