# Python Slot Machine by Raven Cunanan
import random

symbols = ["🍒", "🍇", "🍉","7️⃣"]

play=True

def play():
  global play
  answer = input("Do you want to keep playing? (Y/N)?: ")
  if answer.upper() == "N":
    play = False

while play:
  symbol1=random.choice(symbols)
  symbol2=random.choice(symbols)
  symbol3=random.choice(symbols)
 
  print(str(symbol1) + " |"+ str(symbol2)+ " |"+ str(symbol3))

  if(symbol1==symbol2 and symbol1==symbol3):
    print("Winner")
  elif(symbol1==symbol2==symbol3=="7️⃣"):
    print("Jackpot!")
  else:
    print("Loser!")

  play()



