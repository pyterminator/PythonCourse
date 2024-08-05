def Min_(coxluq):
    if len(coxluq) > 0:
        minimum = coxluq[0]
        for element in coxluq:
            if type(element) == int or type(element) == float:
                if element < minimum: minimum = element
            else: raise Exception("Listin içərisində yalnız float və int olmalıdır.")
        return minimum
    else:
        raise Exception("List boş ola bilməz!")

def Min(x): 
    try: return Min_(coxluq=x)
    except Exception as msj: return msj




my_list = [0, -9, 9, 8, 5.6]
print(
    Min(my_list)
)