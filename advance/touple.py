

# days= ("sunday","monday","tuestday") 


# #touple unpacking 

# day1,day2,day3 = (days) 
# print(day1)


# Function returning two values 

'''def calculato(num1,num2): 
    sum = num1 + num2 
    multiply = num1 * num2
    return sum,multiply

returned_value = calculato(4,5)
sum,multiply = returned_value
print(f"The value of multi is {multiply}")'''

#List inside tuple 

# tuple_a = (1,2,3,4,5,6,7,8,9)

# print(tuple_a)
# print(min(tuple_a))
# print(max(tuple_a))
# print(sum(tuple_a))


'''
searched_value="sth" 
left_pointer = 0 
right_pointer = len(tuple_a)-1 
mid_pointer = (left_pointer + right_poiter)/2 

if value < mid_pointer: 
    right_pointer = mid_pointer  
    
'''

from curses import baudrate


new_tuple = tuple(range(1,11))
print(new_tuple)

create_list_from_tuple = list(new_tuple)
print(f"{create_list_from_tuple}and its type is: {type(create_list_from_tuple)}")
create_string_from_tuple = str(new_tuple)
print(f"The string is: {create_string_from_tuple} and its type is: {type(create_string_from_tuple)}")
a = 10 
