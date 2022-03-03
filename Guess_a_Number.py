#!/usr/bin/python

import random
import sys

print("Please choose a random number between 1 and 10 (with one decimal max):")

def guessnum():
   for number in range(1):
      value = round(random.uniform(1,10), 1)

   number = float(input())

   if number > 10.0:
      print("Please choose a number below 10.0!")
      guessnum()
   elif number == value:
      print("You chose", number, "while your CPU chose", value,":)")
      print("Well... You won!")
   else:
      print("You chose", number, "while your CPU chose", value,":(")
      print("Well... You lost!")

guessnum()

# Rest does not work yet...
"""
print("Want to play again? (y/n)")
again = input()
def play_again():
   if again == 'y':
      guessnum()
   else:
      sys.exit("Bye!")
play_again()
"""