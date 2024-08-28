import pandas

data = pandas.read_csv("users.csv")

print(data["email"].to_list())

# DataFrame - Series