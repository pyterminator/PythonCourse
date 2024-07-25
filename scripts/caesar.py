from string import ascii_lowercase as al
# abcdefghijklmnopqrstuvwxyz - 26
# 01234567890123456789012345


def Sezar_(word:str, key:int, encrypt:bool = True):
    if type(word) == str and type(key) == int and type(encrypt) == bool:
        if len(word) == 0: raise Exception("Söz minimumum 1 simvoldan ibarət olmalıdır!")

        if encrypt:
            new_word = "" 
            for letter in word:
                letter_index = al.find(letter) + key
                if letter_index > len(al) - 1:
                    letter_index = letter_index % len(al)
                new_word += al[letter_index]
            return new_word
        else:
            # Desifre et!
            pass 
    else: 
        raise Exception("Sezar funksiyası üçün göndərilmiş parametrlərin tipləri doğru deyil!")


def Sezar(word:str, key:int, encrypt:bool = True):
    try: return Sezar_(word=word, key=key, encrypt=encrypt)
    except Exception as msg: return msg 



result = Sezar("zer", 3)
print(result)