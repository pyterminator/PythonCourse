import os 

from sqlalchemy import (
        create_engine,
        Column,
        Integer,
        String
    )
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import or_


BASE_DIR = os.getcwd()
BASE = declarative_base()

engine = create_engine(f"sqlite:///{BASE_DIR}/data.db")
Session = sessionmaker(bind=engine)
Session = Session()

class User(BASE):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String(20))
    last_name = Column(String(20))

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name}"

# BASE.metadata.create_all(engine)

# user_1 = User(first_name="Mushvig", last_name="Shukurov")
# user_2 = User(first_name="Eyvaz", last_name="Shukurov")
# user_3 = User(first_name="Natig", last_name="Shukurov")

# Session.add(user_1)
# Session.add(user_2)
# Session.add(user_3)

# Session.add_all([user_2, user_3])

# Session.commit()

# CRUD - Create, Read, Update, Delete 

# users = Session.query(User)
# for user in users:
#     print(user.id)

# user = Session.query(User).filter(User.id == 2).first()

# print(user.id, user.first_name)


# users = Session.query(User).filter(or_(User.id == 2,  User.first_name == "Mushvig"))

# for user in users:
#     print(user)

# user = Session.query(User).filter(User.id == 1).first()

# # print(user)
# Session.delete(user)
# Session.commit()


user = Session.query(User).filter(User.id == 3).first()

user.first_name = "Natiq"

Session.commit()