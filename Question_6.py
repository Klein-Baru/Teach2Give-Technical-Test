sentence = input("Enter an English word/sentence:")
count = 0

characterize = [i for i in sentence]

for character in characterize:

    if character == "a" or character == "A":

        count += 1
        continue

    elif character == "e" or character == "E":

        count += 1
        continue

    elif character == "i" or character == "I":

        count += 1
        continue

    elif character == "o" or character == "O":

        count += 1
        continue

    elif character == "u" or character == "U" :

        count += 1
        continue

    else:

        pass

print(count)






