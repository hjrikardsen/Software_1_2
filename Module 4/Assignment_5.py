username = "python"
password = "rules"

i = 0

while i < 5:

    check_username = input("Enter username: ")
    check_password = input("Enter password: ")

    if check_username == username and check_password == password:
        print("Welcome")
        break
    elif (check_username != username or check_password != password) and i == 4:
        print("Access denied")
        break
    else:
        print("Incorrect username or password. Please try again.")

    i += 1