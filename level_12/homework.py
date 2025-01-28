for i in range(1, 51, 2):
    print(i)

for i in range(5):
    print(10*"*")

for i in range(4):
    print(15*"*")

for num1 in range(1, 4):
    for num in range(1, 4):
        print(num1, num)

a = input("Do you want to start registacion? ")
if a == "yes":
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
else:
    print("Goodbye")