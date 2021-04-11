#!/usr/bin/python

# You are making a Celsius to Fahrenheit converter.
# Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.
# Sample Input
# 36
# Sample Output
# 96.8

print("Enter the temperature in Celsius:")
celsius = float(input())


def conv(c):
    return 9 / 5 * c + 32


fahrenheit = conv(celsius)

print("Your temperature in Fahrenheit:")
print(fahrenheit)
