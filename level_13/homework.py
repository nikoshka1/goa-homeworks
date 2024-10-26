# First task
name = input("Enter your name:")
result = ""

for i in name:
    result += i + " "
print(result)

# Second task

num_1 = int(input("Enter start number:"))
num_2 = int(input("Enter end number:"))

for i in range(num_1, num_2):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "ეს ციფრი არის 3-ისა და 2-ის ჯერადი")
    else:
        print(i, "ეს ციფრი არ არის 3-ისა და 2-ის ჯერადი")

# Trird task

result = 0

for i in range(5):
    num = int(input("Enter number: "))
    result += num
print(result)

# Fourth task 

for i in range(-101, 101):
    if i > 0:
        print(i)

# Fifth task

num = int(input("შეიყვანეთ დადებითი რიცხვი: "))

while num <= 0:
    num = int(input("შეიყვანეთ დადებითი რიცხვი: "))
