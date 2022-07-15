# # list_of_numbers = [1,2,3,4,5]
# # list_of_evennumbers = [2,4,6]
# # list_of_oddnumbers = [1,3,5]


# # mixed = ["one",2,3.0,"Four",False]
# # for i in list_of_evennumbers:
# #     print (f"{i}\n")
# # list_of_oddnumbers[2] = False 
# # print(list_of_oddnumbers[2])

# # print(type(mixed))

# # # 2) add data to list ---> append() method 
# # list_of_numbers = [1,2,3,4,5]
# # list_of_numbers.append(6)
# # list_of_numbers.insert(2,11)  # position = 2 
# # print(list_of_numbers)

# fruits1 = ["apple","mango","banana"]
# fruits2= ["graoes","watermelon","guava","guava"]

# fruits1.pop(0)      #position 

# print(fruits1)

# del fruits1[1]
# print(fruits1) 


# # 4) in keyword in list 
# if "apple" in fruits1: 
#     print("Present")
# else: 
#     print("Absent")

# print(fruits2.count("grapes")) 
# fruits2.sort()
# print(fruits2) 



# fruits2.reverse()
# fruits3 = fruits2.copy() 
# print(fruits2) 

# fruits2.clear()
# print(fruits2) 
# print(fruits3) 

# # Is vs Equal

# fruits5 = ["apple","mango","banana"]
# fruits6 = ["apple","mango","banana"]

# print(fruits5 == fruits6) # Check for same value as well as num 

# print(fruits5 is fruits6) # Check for the location ofobjext in memory i.e RAM 

# def give_me_list(num):
#     my_list = []
#     for i in range(0,num+1):
#         my_list.append(i)
#     return my_list

# mero_list = give_me_list(10) 
# print (mero_list)


        
'''def qs(num): 
    my_list = [] 
    for i in range(0,num+1):
        my_list.append(i**2)
    return my_list

mero_list = int(input("Enter number")) 
alu = qs(mero_list)
print (alu)'''

# def rev(wau):
#   wau.reverse() 
#   return wau

# poteto = rev(alu)
# print(poteto)



'''def revlist(givenlist):
    reversed_list = []
    for item in givenlist:
        poppwed_item = givenlist.pop() 
        reversed_list.append(poppwed_item)
    return reversed_list'''


# any = ["aryama","kritika","rushav","samay","maharshi"]
# def rev (wau): 
#     reved = []
#     for i in wau:
#         reved.append(i[::-1])
#     return reved
    
# reved = rev(any)
# print(reved)


num = int(input("Enter a num: "))
# def given_listed(input_num): 
#     list = [] 
#     for items in input_num: 
#         ans = items()
a = list(range(0,num+1))

def qs(abc): 
    my_list1 = [] 
    my_list2 = [] 
    for i in abc:
        if i%2 == 0: 
            my_list2.append(i)
        else:
            my_list1.append(i)
    return [my_list1,my_list2] 



wau = qs(a)
print(wau)
    
def counter(daf): 
    count = 0 
    for i in daf:
        if type(daf) == list: 
            count = count + 1
    return count
    

uwu = counter(wau) 
print(uwu) 



