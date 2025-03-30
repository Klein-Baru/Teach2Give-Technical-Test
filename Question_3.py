#  Question 3: Power of Two
#  Write a program that takes an integer as input and returns true if the input is a power of two.

import math

user_input = int(input("Enter any number: "))

power_of_two = math.log2(user_input)

print(power_of_two.is_integer())
