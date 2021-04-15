#!/usr/bin/python

# Given a text as input, find and output the longest word.
# Sample Input:
# this is an awesome text
# Sample Output:
# awesome

print("Please enter your text so this little program can find the longest word:")
txt = input().split()

length = [len(x) for x in txt]
max_length = max(length)
txt_index = length.index(max_length)

print("The longest word is:")
print(txt[txt_index])
