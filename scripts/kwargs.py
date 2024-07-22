def Topla(*args, **deyerler):
    print(args)
    print("--------------------------")
    total = 0
    for (key, value) in deyerler.items(): 
        print(key+": ", value, sep="")
        total += value
     
    return total

cem = Topla(7, 4, 5 , a=1, c=2, b=3) 
print(cem ** 2)