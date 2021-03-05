from replit import db
import random


class Ranking:
  def __init__(self, seed = 420):
    self.seed = seed

  #Give user a random amount of exp and create entry for ne users
  def exp_gift(self, name):
    db_keys = db.keys()
    if (name + "_exp") not in db_keys:
      db[name + "_exp"] = 0
    db[name + "_exp"] = db[name + "_exp"] + random.randint(1, 50)

  #Print out a user's current exp
  def status(self, name):
    return "EXP: " + str(db[name + "_exp"])
    