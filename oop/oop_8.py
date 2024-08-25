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
# Serialize - Deserialize


class User:
    caesar_key = 5
    user_count = 0
    person_list = list() 

    def __init__(self, name:str, surname:str):
        User.user_count += 1
        self.id = User.user_count
        self.name = name
        self.surname = surname 

        User.person_list.append(self)

    def __str__(self): 
        return "{id},{name},{surname},{password}".format(
            id=self.id, 
            name=self.name, 
            surname=self.surname,
            password=self.__password)

    @property
    def get_password_encrypt(self): return self.__password

    @property
    def get_password(self): return Sezar(self.__password, User.caesar_key, False)

    @get_password.setter
    def set_password(self, password):
        self.__password = Sezar(password, User.caesar_key)
    

    @classmethod
    def To_CSV(cls):
        fayl = open("person.csv","w+", encoding="utf-8")
        fayl.write("ID,Name,Surname,Password\n") 
        for user in cls.person_list:  
            fayl.write(str(cls.__str__(user))+"\n")
        fayl.close()

    @classmethod
    def GetUser(cls):
        with open("person.csv","r", encoding="utf-8") as file:
            file.readline()
            data = file.readlines()
            data = [str_user.strip("\n").split(",") for str_user in data]
            for user_data in data: 
                new_user = cls(user_data[1], user_data[2]) 
                new_user.id = int(user_data[0])
                new_user.set_password = Sezar(user_data[3], cls.caesar_key, False)

User.GetUser()


for person in User.person_list:
    print(person.get_password)









# person_1 = Person("Mushvig", "Shukurov")
# person_1.set_password = "123456"

# person_2 = Person("Eyvaz", "Shukurov")
# person_2.set_password = "123456"

# person_3 = Person("Natig", "Shukurov")
# person_3.set_password = "123456"

# Person.To_CSV()