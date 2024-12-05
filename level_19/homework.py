letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']

num = 0

for i in range(len(letters)):
        if letters[i] in vowels:
            num += 1

print(num)


numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]

for i in numbers:
    if i % 5 == 0 and i % 3 == 0:
        print(i, "5-ისა და 3-ის ჯერადია")

list = ["f", "s", "w", "e" , 1, 2, 3, 4]

for i in range(len(list)):
    if type(list[i]) == int:
        list[i] = str(list[i])

print(list)

symbol = "*"

for i in range(n):
    print(" " * i + symbol * 6)

age = int(input("ჩაწერე შენი ასაკი: "))
if age < 12:
    print("შენ არ ხარ 12 წლის")

