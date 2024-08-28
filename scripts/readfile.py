import csv 


with open("users.csv", "r") as file:
    header = file.readline()
    # data = file.read() 
    # data = file.readlines()
    email_list = []
    data = csv.reader(file)
    for row in data: email_list.append(row[3])

    print(email_list)
