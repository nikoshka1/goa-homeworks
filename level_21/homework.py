list_of_names = ["დავით", "გიო", "ანა", "დავით", "მარიამ", "დავით"]
name_to_count = "დავით"
count = 0

for i in range(len(list_of_names)):
    if list_of_names[i] == name_to_count:
        count += 1

print("სახელი დავეთ მეორდება", count, "ჯერ")

numbers = [1, 2, 3, 4, 5]
numbers.reverse()  
print(numbers)

list_of_numbers = [1, 2, 3]
length = len(list_of_numbers)
result = list_of_numbers * length
print(result)

insert_arr = ["python", "CSS", "JAVASCRIPT"]
insert_arr.insert(1, "C#")
print(insert_arr)

numbers = [1, 2, 3, 2, 4, 2]
element_to_remove = 2

count = numbers.count(element_to_remove)
numbers.remove(element_to_remove)
print("ელემენტი", element_to_remove, "მეორდება", count, "ჯერ.")
print("განახლებული სია:", numbers)