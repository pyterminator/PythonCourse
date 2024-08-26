"""
Inheritance
Encapsulation
Abstraction
Polymorphism
"""
from abc import ABC, abstractmethod

class BaseUser(ABC):
    
    @abstractmethod
    def bio(self):pass 
    
    @abstractmethod
    def About(self):pass 


class User(BaseUser):
    def bio(self): pass 
    def About(self): pass

user_1 = User()

# ---------------------------------------------------------------------



# class User:

#     def About(self): return "Salam dunya!"

# class Customer(User):
    
#     def About(self):
#         print("Salam dunya!")

# user_1 = User()
# customer_1 = Customer()


# my_list = [user_1, customer_1]


# for element in my_list:
#     print(element.About())


# ---------------------------------------------------------------------

# class User:

#     def __init__(self, name:str, surname:str):
#         self.name = name 
#         self.surname = surname  
#         self._username = self.name + self.surname
         
#     @property
#     def bio(self): return self.__bio

#     @bio.setter
#     def bio(self, bio:str):
#         self.__bio = bio
    
#     @bio.deleter
#     def bio(self):
#         self.__bio = ""

#     def __str__(self):
#         return f"{self.name} {self.surname} {self.bio}, {self._username}"




# user_1 = User("Mushvig", "Shukurov")
# user_1.bio = "Salam, Adım Müşviqdir sds sf s...."

# user_2 = User("Eyvaz", "Shukurov")
# user_2.bio = "Salam, Adım Eyvazdır sds sf s...."

# user_3 = User("Natiq", "Shukurov")
# user_3.bio = "Salam, Adım Natiqdir sds sf s...."


# user_1.name = "Mushviq"

# del user_1.bio
# del user_2.bio

# user_1._username = "214234234"

# print(user_1)
# print(user_2)
# print(user_3)