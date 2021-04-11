#!/usr/bin/python

# Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
# It’s calculated using a person's weight and height, using this formula: weight / height²
# The resulting number indicates one of the following categories:
# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more
# Let’s make finding out your BMI quicker and easier,
# by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.
# Sample Input
# 85
# 1.9
# Sample Output
# Normal

print("Enter your weight in kilograms:")
weight = float(input())
print("Enter your height in meters (for example: 1.70):")
height = float(input())

bmi = weight / (height * 2)

if bmi < 18.50:
    print("You are underweight!")
elif bmi >= 18.50 and bmi < 25.0:
    print("Your weight is normal!")
elif bmi >= 25.0 and bmi < 30.0:
    print("You are overweight!")
else:
    print("You are obese!")
