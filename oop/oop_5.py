def Sezar_(word:str, key:int, encrypt:bool = True):
    al = "2ezğwxtörvqb6ABCDEFGHIJKLMNOPQRSTUVWXYZdhlp1şf0ac3gəün9u7ym5osiıç8k4jŞÇƏİĞÖÜ"
    al = al + al.upper()

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
            new_word = ""
            for letter in word:
                letter_index = al.find(letter) - key 
                if letter_index < 0:
                    letter_index = letter_index + len(al)
                new_word += al[letter_index]
            return new_word
    else: raise Exception("Sezar funksiyası üçün göndərilmiş parametrlərin tipləri doğru deyil!")

def Sezar(word:str, key:int, encrypt:bool = True):
    try: return Sezar_(word=word, key=key, encrypt=encrypt)
    except Exception as msg: return msg 



class User:  
    caesar_key = 5
    user_count = 0
    users_list = list() 

    def __init__(self, name, surname):
        User.user_count += 1
        self.id = User.user_count
        self.name = name
        self.surname = surname 

        User.users_list.append(self)

    def __str__(self): 
        return "{id},{name},{surname},{password}".format(
            id=self.id, 
            name=self.name, 
            surname=self.surname,
            password=self.__password)

    def SetPassword(self, password):
        self.__password = Sezar(password, User.caesar_key)
    
    def GetPassword(self):
        print(Sezar(self.__password, User.caesar_key, False))

    @classmethod
    def To_CSV(klass):
        fayl = open("users.csv","w+", encoding="utf-8")
        fayl.write("ID,Name,Surname,Password\n") 
        for user in klass.users_list:
            fayl.write(str(user)+"\n")
        fayl.close()

user_1 = User("Mushvig", "Shukurov")
user_1.SetPassword("12345")
user_1.__password = "Salam"
user_1.SetPassword("1234554321")

User.To_CSV()