# first and second task
age = int(input("Enter your age:"))
is_A = print(age >= 9)
is_b = print(8 <= age < 9)
is_C = print(7 <= age < 8)
is_D = print(6 <= age < 7)
is_F = print(age < 6)

# third task
a = True
b = False

print(a and b)
print(a or b)

# fourth task
first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))

print(first_number < second_number)
print(first_number > second_number)
print(first_number <= second_number)
print(first_number >= second_number)
print(first_number == second_number)
print(first_number != second_number)

# fifth task
z = int(input("Enter first number:"))
x = int(input("Enter second number:"))
c = int(input("Enter third number:"))

is_z_biggest = print(z > x > c or z > c > x)
is_x_middle = print(c < x < z or z < x < c)
is_c_least = print(c < x < z or c < z < x)

# sixth task 
score = int(input("Enter your score:"))
is_pass = print(score >= 50)
is_high_pass = print(75 < score < 90)
is_perfect = print(score == 100)
is_failing = print(score < 50)
