# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence

sentence = input("Enter an English word/sentence:")
count = 0
dont_repeat_a = 0
dont_repeat_e = 0
dont_repeat_i = 0
dont_repeat_o = 0
dont_repeat_u = 0

characterize = [i for i in sentence]

for character in characterize:

    if (character == "a" or character == "A") and dont_repeat_a == 0:

        count += 1
        dont_repeat_a = 1
        continue

    elif (character == "e" or character == "E") and dont_repeat_e == 0:

        count += 1
        dont_repeat_e = 1
        continue

    elif (character == "i" or character == "I") and dont_repeat_i == 0:

        count += 1
        dont_repeat_i = 1
        continue

    elif (character == "o" or character == "O") and dont_repeat_o == 0:

        count += 1
        dont_repeat_o = 1
        continue

    elif (character == "u" or character == "U") and dont_repeat_u == 0:

        count += 1
        dont_repeat_u = 1
        continue

    else:

        pass

print(count)












