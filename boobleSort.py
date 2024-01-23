def sort():
    number_list = [5, 3, 6, 1, 6, 10, 22, 43, 55, 12]

    list_size = len(number_list)

    for i in range(list_size):
        for j in range(0, list_size - i -1):
            if(number_list[j] > number_list[j + 1]):
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
                print(number_list)
    
    return number_list

print(sort())