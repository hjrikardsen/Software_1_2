names = set()

isTrue = True

while isTrue:
    name = input("Enter a name: ")

    if name != "":
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)
    else:
        isTrue = False

for i in names:
    print(i)
