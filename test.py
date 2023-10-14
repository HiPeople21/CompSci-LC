print(f"{'_' * 30}Height Calculator{'_' * 30}")
prompt = input("Press y to continue, any other key to exit: ")
if prompt.lower() != "y":
    exit()
while prompt == "y":
    gender= input("Enter the gender of your future child. Use 1 for female, 0 for male: ")
    while gender not in ("0", "1"):
        gender= input("Re-enter the gender of your future child. Use 1 for female, 0 for male: ")
    gender = int(gender)      
    print("Enter the height in feet then the height in inches of the Mom.")
    while True:
        mother_feet = input("Feet: ")
        if mother_feet.isdigit():
            mother_feet = int(mother_feet)    
            break
    while True:
        mother_inches = input("Inches: ")
        if mother_inches.isdigit():
            mother_inches = int(mother_inches)    
            break       

    print("Enter the height in feet then the height in inches of the Dad.")
    while True:
        father_feet = input("Feet: ")
        if father_feet.isdigit():
            father_feet = int(father_feet)    
            break
    while True:
        father_inches = input("Inches: ")
        if father_inches.isdigit():
            father_inches = int(father_inches)    
            break
        
    if gender == 1:
        height = ((((father_feet * 12) + father_inches) * 12/13) + (mother_feet * 12) + mother_inches)/2
        print(height)
        print(f"Your future child is estimated to grow to {int(height / 12)} feet and {int(height % 12)} inch(es)")
    else:
        height = ((((mother_feet * 12) + mother_inches) * 13/12) + (father_feet * 12) + father_inches)/2
        print(height)
        print(f"Your future child is estimated to grow to {int(height / 12)} feet and {int(height % 12)} inch(es)")

    prompt = input("Enter y to run again, anything else to exit: ")