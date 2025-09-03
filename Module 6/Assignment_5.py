def filter_even_numbers(list):
    for i in list:
        if i % 2 != 0:
            list.remove(i)
    return list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {list1}")

list2 = filter_even_numbers(list1)

print(f"List with even numbers only: {list2}")