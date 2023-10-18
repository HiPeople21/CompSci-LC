import time

dob = input("Your DOB (dd/mm/YYYY): ")
day, month, year = map(int, dob.split("/")
)
# Check month validity
if not(1 <= month <= 12):
    raise ValueError(f"Invalid month ({month})")

# Check date validities
if month in (1, 3, 5, 7, 8, 10, 12) and not 1 <= day <= 31:
    raise ValueError(f"Invalid day ({day}) for month ({month})")
if month in (4, 6, 9, 11) and not 1 <= day <= 30:
    raise ValueError(f"Invalid day ({day}) for month ({month})")
if month == 2 and not 1 <= day <= 28 and year % 4 != 0:
    raise ValueError(f"Invalid day ({day}) for month ({month})")
if month == 2 and not 1 <= day <= 29 and year % 4 == 0 :
    raise ValueError(f"Invalid day ({day}) for month ({month})")

today = time.localtime()
age = today.tm_year - year
if today.tm_mon - month <= 0:
    if today.tm_day - day <= 0:
        age -= 1

    
print(f"You are {age} years old.")