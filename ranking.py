from replit import db


class Ranking:
  def __init__(self, seed = 420):
    self.seed = seed

  def name_checker(self, name):
    db_keys = db.keys()
    if name not in db_keys:
      print("lll")
    