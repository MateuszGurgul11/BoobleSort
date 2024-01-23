n = int(input("Wpisz wielkosc listy: "))
number_list = []

for add_list in range(n):
    number = int(input("Wpisz liczbe: "))
    number_list.append(number)

list_size = len(number_list)

for i in range(list_size):
    for j in range(0, list_size - i -1):
        if(number_list[j] > number_list[j + 1]):
            number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
            print(number_list)
    


