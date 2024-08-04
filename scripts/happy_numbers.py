def EdedinBolenleri(number):
    my_list = []
    for num in range(1, number+1):
        if number % num == 0:
            my_list.append(num)
    return my_list


def HappyNumber(num):
    ededin_bolenleri = EdedinBolenleri(num)
    ededin_bolenleri.pop()
    total = sum(ededin_bolenleri)
    if total == num: return True 
    return False



my_list = list(range(1, 100))


happy_numbers = list(filter(HappyNumber, my_list))

print(happy_numbers)