# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

values = list()
fib_sequence = []
iterator = -1

for i in range(0, 101):

    values.append(i)

for value in values:

    if value == 0:

        fib_sequence.append(value)

    elif value == 1:

        iterator += 1

        fib_sequence.append(value + values[iterator])

    else:

        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])

print(fib_sequence)
