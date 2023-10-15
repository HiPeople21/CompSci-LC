words = input("Please enter three words, separated by spaces: ").strip()
if words.count(" ") != 2:
    print(f"Invalid amount of words: {words.count(' ') + 1}")
    exit()

print(f"The abbreviation of '{words}' is {''.join(map(lambda x: x[0].upper(), words.split(' ')))}.")