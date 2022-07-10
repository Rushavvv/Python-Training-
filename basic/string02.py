# # # # # # #Excersise 
# # # # # first_name,second_name = input("please provide your full name:").split (" ") 
# # # # # name_type = type(first_name) 
# # # # # print("Your full name is "+ first_name +" "+second_name)
# # # # # print("Type of your first name is "+ name_type)
# # # # num_1,num_2,num_3 = input("Please input the three numbers;").split(",") 
# # # # a = int(num_1) + int(num_2) + int(num_3) 
# # # # print(a//3)

# # # # String Indexing 
# # name = "language"
# # # print(name[3:8]) -----> gives output guage last ko exclusive huncha
# # print (name[::-1]) #reverse didincha 
# # example = "leArN pYtHon"
# # print(example.lower())
# # print(example.upper())
# # print(example.title())
# # # # print(example.count("p")) #----> kati ota cha bhanha 

# name,character = input("Input your full name and character").split(",")

# # print("Your fullname is " + name + " the number of characters are " + str(name.lower().count(character)))
# # # '''
# # # OR

# # '''
# char_count = name.lower().count(character.strip())

# print("Your fullname is {} and '{}' char count is {}".format(name,character,char_count))  #This is added in python 3

# # print("Your fullname is {name} and '{character}' char count is {char_count}") #this was added in python 3.6

# print(f"Your fullname is {name} and '{character}' char count is {char_count}")

'''
space problems

'''



# spaces_prob = "    Rushav    "
# stars = "********"
# print(stars+spaces_prob.strip()+stars) 

# solved_problem = spaces_prob.replace(" ","")

# print(f"The solve of space problem is {solved_problem}")



#Finding and replacing a string 

'''
replace_example = "Kritika is beautiful and she is out standing "
print(replace_example.replace("is","was",1))
is_pos1= replace_example.find("is")
print(replace_example.find("is",is_pos1+1))
'''

#Center() Method 

# example2 = "python"
# print(example2.center(4+6+4,"*"))
'''
name = input("Enter your name")
sol = len(name)
print(name.center(5+sol+5,"*"))
'''



## String are immutable and assignment operator 

'''
example3 = "any" 
example3[1] = "N"  #can't do because of immutable 

'''

# example = example + "body"    ra    example += "body" garnu eutai ho 

