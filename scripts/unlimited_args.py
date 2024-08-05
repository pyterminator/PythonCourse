def Topla(*args):
    sum = 0
    for element in args:
        sum += element
    return sum 

print(Topla(4,5,3,4,1,2,3))