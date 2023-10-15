import random

num = random.randint(1, 5)
print(f"Random number: {num}")
sum_ = 0
product = 1
for i in range(1, num + 1):
    sum_ += i
    product *= i
    
print(f"Sum: {sum_}")
print(f"Product: {product}")
