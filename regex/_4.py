import re 

# d - digit

text = "Lorem Ipsum is simply dummy 16781679"

my_list = re.findall(r"\d+$",text)

print(my_list)