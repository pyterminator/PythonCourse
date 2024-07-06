print("Oyun başladı!")
from random import randint
from termcolor import colored as rengle

(minimum, maksimum) = (0, 10)

next_game = True
score = 0 

while True:
    if next_game: 
        random_eded = randint(minimum, maksimum)
        next_game = False 
 
    print(rengle("[0, 10] aralığında bir ədədi fikrimdə tutdum. Ədədi tap.", color="green"))

    command = input("Sənin təxminin : ")

    if command == "exit": break 
    elif command == str(random_eded): 
        next_game = True
        score += 1
        print(rengle("Bəli, fikrimdə tutduğum ədəd {0} idi.".format(random_eded),"cyan"))
    else: 
        try:
            number = int(command)
            if number > random_eded:
                print(rengle("Daxil etdiyin ədəd fikrimdə tutduğum ədəddən böyükdür.", "light_yellow"))
                continue
            else:
                print(rengle("Daxil etdiyin ədəd fikrimdə tutduğum ədəddən kiçikdir.", "light_yellow"))
                continue
        except: 
            print("Doğru istifadə et.")
            continue

print("Sizin topladığınız xal :", score)
print("Oyun dayandırıldı!")