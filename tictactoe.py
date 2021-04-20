from replit import db
import discord

################################
# - Check for move overriding existing things
# - Check for out of bounds Coordinates
# - Check coordinate validation when using "move"
# - Understand when the game is won.
# - 


################################

class TicTacToe:
  def __init__(self, seed = 42069):
    self.seed = seed
    self.o = True

  def resolver(self, message):
    if(message[0] == "new"):
      self.newGame()
      return self.toString()
    elif(message[0] == "board"):
      return self.toString()
    elif(message[0] == "move"):
      if(len(message) < 3):
        return "No Coordinates"
      else:
        coord = [int(message[1]), int(message[2])]
        self.move(coord)
        return self.toString()
    

  #Reset the Board, "ttt" is used to access the board in the database.AttributeError
  def newGame(self):
    self.o = True
    db['ttt'] = [[None, None, None], [None, None, None], [None, None, None]]
    

  def move(self, coord):
    board =  db['ttt']
    if(self.o):
      board[coord[0]][coord[1]] = True
      self.o = False
    elif(self.o == False):
      board[coord[0]][coord[1]] = False
      self.o = True
    db["ttt"] = board


  def toString(self):
    board = "-------------- \n"
    for x in db['ttt']:
      for y in x:
        if(y == True):
          board = board + " O  | "
        elif(y == False):
          board = board + " X  | "
        else:
          board = board + "    | "
      board = board + "\n"
      board = board + "-------------- \n"
      
    return board