user_input2 = input()

characterize = [i for i in user_input2]
count = -1

for i in characterize:

    count += 1

    first_character = characterize[0].upper()
    characterize.pop(0)
    characterize.insert(0, first_character)

    if i == " ":

        letter = characterize[count + 1].upper()
        characterize.pop(count + 1)
        characterize.insert(count + 1, letter)

count2 = 0
capitalized = ""
for i in characterize:

    capitalized += i

print(capitalized)
