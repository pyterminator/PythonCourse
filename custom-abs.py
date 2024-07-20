import math

def Abs(a): 
    if type(a) == complex:
        real = a.real 
        imag = a.imag
        return math.sqrt(real ** 2 + imag ** 2)
    else:
        if type(a) == int or type(a) == float:
            if a < 0: return a * -1
            else: return a
        else: 
            raise Exception("INT, Complex, Float daxil et!")

    

try:
    result = Abs(-5) 
    print(result)
except Exception as e:
    print(e)