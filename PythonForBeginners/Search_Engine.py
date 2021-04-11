#!/usr/bin/python

# You’re working on a search engine. Watch your back Google!
# The given code takes a text and a word as input and passes them to a function called search().
# The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.
# Sample Input
# "This is awesome"
# ""awesome"
# Sample Output
# Word found

print("Enter the text you want to search:")
text = input()

print("Enter the word you want to search for:")
word = input()


def search():
    if text.find(word) == -1:
        print("Word not found")
    else:
        print("Word found")


search()
