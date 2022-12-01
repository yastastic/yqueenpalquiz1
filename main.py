number_list = list(range(0, 200))

for number in number_list[ : : -1]:
    if number%3 == 0:
        print(number)

