# Is | Is Not
def Sum(*args):
    total = 0
    for element in args: 
        # if type(element) is not int or type(element) is not float:
        #     raise Exception("Sadəcə integer və float daxil edin!")
        # else: total+=element
        if type(element) is int or type(element) is float: total += element 
        else: raise Exception("Sadəcə integer və float daxil edin!")
    return total

try: print(Sum(8,9,1,90.))
except Exception as message: print(message)