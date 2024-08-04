class User:  
    user_count = 0 # class variable
    def __init__(self, name, surname):
        User.user_count += 1
        self.id = User.user_count
        self.name = name # instance variable
        self.surname = surname 
    
    def About(self): print(self.id, self.name, self.surname, sep=",") 

user_1 = User("Mushvig", "Shukurov") # instance
user_2 = User("Eyvaz", "Shukurov")
user_3 = User("Natiq","Shukurov")

user_1.About()
user_2.About()
user_3.About()

print(
    User.user_count
)