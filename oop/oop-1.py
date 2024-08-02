class User: 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def About(self): print(self.name, self.surname) 
     




user_1 = User("Mushvig", "Shukurov")
user_2 = User("Eyvaz", "Shukurov")
 

user_1.About()
user_2.About()
