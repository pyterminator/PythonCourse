from getpass import getpass

db = {
    "username":"mushvig",
    "password":"1234"
}

username = input("İstifadəçi adınızı daxil edin :")
password = getpass("Şifrənizi daxil edin :")


if db.get("username", None) == username and db.get("password", None) == password:
    print("Xoş gəldin")
else:
    print("İstifadəçi adı və ya şifrə yanlışdır.")