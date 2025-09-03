def sum_of_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum


list_int = [1, 2, 3, 4, 5]

print(f"The sum of the numbers in the list is: {sum_of_list(list_int)}")