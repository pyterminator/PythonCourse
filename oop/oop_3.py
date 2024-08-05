class User:  
    user_count = 0 # class variable 
    users_list = list() 
    def __init__(self, name, surname):
        User.user_count += 1
        self.id = User.user_count
        self.name = name # instance variable
        self.surname = surname 

        User.users_list.append(self)

    def __str__(self): return "{id},{name},{surname}".format(id=self.id, name=self.name, surname=self.surname)


user_1 = User("Mushvig", "Shukurov") # instance
user_2 = User("Eyvaz", "Shukurov")
user_3 = User("Natiq","Shukurov")
user_4 = User("Akif","Alakurt")
user_5 = User("Hector","William")
user_6 = User("Ravan","Mammadov")


for element in User.users_list:
    print(element)