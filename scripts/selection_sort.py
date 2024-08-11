# Selection Sort
my_list = [9,3,8,1,2,0,4,6,5,7] 


for index in range(0, len(my_list)):
    minimum_index = index
    for inner_index in range(index+1, len(my_list)):
        if my_list[minimum_index] > my_list[inner_index]:
            minimum_index = inner_index
    
    my_list[index], my_list[minimum_index] = my_list[minimum_index], my_list[index]

print(my_list)
    