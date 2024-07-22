from string import ascii_lowercase as al
from random import shuffle

def RPG(length):
    al_list = list(al)
    shuffle(al_list)
    al_string = "".join(al_list)
    password = al_string[0:length]
    
    print(password)
    return password


password_7 = RPG(7)