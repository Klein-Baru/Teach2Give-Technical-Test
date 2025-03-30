import math

user_input = int(input("Enter any number: "))

power_of_two = math.log2(user_input)

print(power_of_two.is_integer())