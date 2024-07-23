# def Dongu(start, stop):
#     print(start) # 0 1 2 3 4 5 6 7 8 9 10
#     if start < stop: Dongu(start+1, stop)
# Dongu(0, 10)


def Faktorial(number, result=1):  
    if number > 1: 
        result = result * number
        Faktorial(number-1, result)
    if number == 1 or number==0: print(result)

Faktorial(5)
Faktorial(4)
Faktorial(3)
Faktorial(2)
Faktorial(1)
Faktorial(0)
Faktorial(-1)