number = int(input("შეიყვანეთ ციფრი: "))

if number % 2 == 0:
    print(number, "არის ლუწი.")
else:
    print(number, "არის კენტი.")

for i in range(1, 101):
    if i % 2 == 0:
        print(i, "არის ლუწი")
    else:
        print(i, "არის კენტი")