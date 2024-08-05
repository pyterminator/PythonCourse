def EdedinBolenleri(number):
    my_list = []
    for num in range(1, number+1):
        if number % num == 0:
            my_list.append(num)
    return my_list


print(
    EdedinBolenleri(5),
    EdedinBolenleri(20),
    EdedinBolenleri(30),
    sep = "\n"
)