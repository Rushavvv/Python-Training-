name = input("Enter your name")
a = 0 
while a < len(name): 
    print(f"{name[a]}: {name.lower().count(name[a].lower())}")
    a += 1 




