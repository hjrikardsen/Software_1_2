list_number = []
user_input = input("Enter a number: ")

while user_input != "":
    list_number.append(float(user_input))
    user_input = input("Enter a number: ")

list_number.sort(reverse=True)

print("The greatest numbers in descending order:")
counter = 0
for i in list_number:
    if counter == 5:
        break
    else:
        print(i)
        counter += 1
