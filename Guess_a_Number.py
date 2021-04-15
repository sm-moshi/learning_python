#!/usr/bin/python

import random

print("Please choose a number between 1 and 1000000:")

for x in range(1):
   value = random.randint(1,1000000)

number = int(input())

if number > 1000000:
   print("Please choose a number below 1000000!")
elif number == value:
   print("You chose:", number )
   print("Your CPU chose:", value )
   print("You won!")
else:
   print("You chose:", number )
   print("Your CPU chose:", value )
   print("You lost!")
