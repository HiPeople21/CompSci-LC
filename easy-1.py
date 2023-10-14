# Version 1
i = 50
j = 51
while j < 101:
    i += j
    j += 1
print(i)

# Version 2

i = 50

for j in range(51, 101):
    i += j
print(i)