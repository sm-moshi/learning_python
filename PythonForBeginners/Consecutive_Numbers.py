#!/usr/bin/python

# No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.
# Let’s save some time by creating a program to do the calculation for you!
# Take a number N as input and output the sum of all numbers from 1 to N (including N).
# Sample Input
# 100
# Sample Output
# 5050
# Explanation: The sum of all numbers from 1 to 100 is equal to 5050.

print("Please enter a number.")
print("This program will output the sum of all numbers from 1 to your number.")
N = int(input())

sum_of_list = sum(range(0, N + 1))

print("Your sum is:")
print(sum_of_list)
