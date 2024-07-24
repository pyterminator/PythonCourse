"""
number : 5
faktorial : 1

number : 4
faktorial : 5

number : 3
faktorial : 20

number : 2
faktorial : 60

number : 1
faktorial : 120


"""

def Faktorial(number, faktorial = 1):  
    if number <= 1: return faktorial 
    return Faktorial(number-1, faktorial=faktorial*number)

print(
    Faktorial(0),
    Faktorial(1),
    Faktorial(5), 
)


# def Faktorial(number):
#     faktorial = 1
    
#     if number > 1:
#         for element in range(1, number+1): faktorial *= element
    
#     return faktorial

# print(
#     Faktorial(5),
#     Faktorial(0),
#     Faktorial(1),
#     Faktorial(4)
# )
