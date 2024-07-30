def TypeControl(funksiya):
    def icerideki_funksiya(x, y):
        my_list = [int, float]
        if type(x) in my_list and type(y) in my_list:
            return funksiya
        raise Exception("a və b int ya da float olmalıdır.")
    return icerideki_funksiya

@TypeControl
def Topla(a, b): return a + b
     
@TypeControl
def Vurma(a, b): return a * b

@TypeControl
def Bolme(a, b): return a / b 

print(
    Bolme(20, "2")
)