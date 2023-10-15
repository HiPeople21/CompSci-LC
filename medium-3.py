name = input("Enter your full name (firstname surname): ")

if name.count(" ") != 1:
    print("Format enter incorrect.")
    exit()
    
print(f"Name: {name.title()}")
print(f"Initials: {''.join(map(lambda x: x[0].upper(),name.split(' ')))}")