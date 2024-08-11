from math import sqrt
my_list = [9, 25, 16, 64, 49, 121, 225]



# List Comprehension

# new_list = [int(sqrt(item)) for item in my_list]
# print(new_list)



# map()
new_list = list(map(sqrt, my_list))
print(new_list)



# Loop

# new_list = []
# for element in my_list:
#     new_list.append(int(sqrt(element)))
# print(new_list)