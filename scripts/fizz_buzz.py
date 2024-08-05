"""
FizzBuzz
Ədəd 3-ə bölünərsə Fizz
5-ə bölünərsə Buzz
həm 3 həm də 5-ə bölünərsə FizzBuzz
Yoxsa da ədədin özünü yazdır
"""

def FizzBuzz(start=0, stop=100): 
    for num in range(start, stop):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else: print(num)

if __name__ == "__main__":
    FizzBuzz(5, 30)