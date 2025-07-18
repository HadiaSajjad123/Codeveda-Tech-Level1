import random

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS =5

def difficulty():
  while True:
    level=input("Choose your difficulty level. Type 'easy' or 'hard'\n")
    if level=="easy":
        print(F"You have {EASY_LEVEL_TURNS} attempts remaining to guess the number")
        return EASY_LEVEL_TURNS
    elif level=="hard":
        print(f"You have {HARD_LEVEL_TURNS} attempts remaining to guess the number")
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input\n")

def check_answer(guess,number,turns):
  if guess > number:
    print("Too high\n")
    return turns - 1
  elif guess < number:
    print("Too low\n")
    return turns - 1 
  else:
    print(f"You got it! the answer was: {guess} \n")
    
def game():   
  print("Welcome to number guessing game!\n")
  start=input("Press enter to start a game\n")
  print("I'm thinking of a number between 1 and 100\n")
  number=random.randint(1,100)
  turns=difficulty()
  
  guess=0
  while guess!=number:
    guess=int(input("Make a guess\n"))
    turns=check_answer(guess,number,turns)
    print(f"You have {turns} attempts remaining to guess the number\n")
    if turns==0:
      print("You've run out of guesses, you lose\n")
      return 
    elif guess!=number:
      print("Guess Again!")
game() 
