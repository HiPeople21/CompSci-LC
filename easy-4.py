while True:
    try:
        euro = float(input("Enter Euro amount: "))
    except ValueError:
        print("Please enter a valid value")
    if euro == 0:
        break
    else:
        print(f"€{euro} = {euro * 120.77} Yen")
    