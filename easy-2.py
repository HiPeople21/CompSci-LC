num = 0
for _ in range(5):
    while True:
        try:
            num += float(input("Floating point number: "))
            break
        except ValueError:
            print("Please enter a floating point number")
    
print(num / 5)