user_input2 = input("Enter any number: ")
user_input2 = [numeral for numeral in user_input2]

count = 1

inverted_list = []

for item in user_input2:

    item = user_input2[len(user_input2)-count]
    count += 1

    inverted_list.append(item)


inverted_str = ""

for item in inverted_list:

    inverted_str += item

if "-" in inverted_str:
    inverted_str = inverted_str.removesuffix("-")
    print(int(inverted_str) * -1)

else:
    print(int(inverted_str))


