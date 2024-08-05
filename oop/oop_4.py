class User:  
    user_count = 0
    users_list = list() 

    def __init__(self, name, surname):
        User.user_count += 1
        self.id = User.user_count
        self.name = name
        self.surname = surname 

        User.users_list.append(self)

    def __str__(self): 
        return "{id},{name},{surname}".format(
            id=self.id, 
            name=self.name, 
            surname=self.surname)

    @classmethod
    def To_CSV(klass):
        fayl = open("users.csv","w+", encoding="utf-8")
        fayl.write("ID,Name,Surname\n") 
        for user in klass.users_list:
            fayl.write(str(user)+"\n")
        fayl.close()

user_1 = User("Mushvig", "Shukurov")
user_2 = User("Eyvaz", "Shukurov")
user_3 = User("Natiq","Shukurov")
user_4 = User("Akif","Alakurt")
user_5 = User("Hector","William")
user_6 = User("Ravan","Mammadov")

User.To_CSV()
