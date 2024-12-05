text = "Hi I am Niko"
a = " "
result = []
word = ""

for i in text:
    if i == a:
        if word:
            result.append(word)
            word = ""
    else:
        word += i

if word:
    result.append(word)

print(result)

words = ["Hi,", "I", "am", "Niko"]
delimiter = " "
result = ""

for i in range(len(words)):
    if i != 0:
        result += delimiter
    result += words[i]

print(result)

text = "Hello world"
old = "world"
new = "Python"
result = ""
i = 0

while i < len(text):
    if text[i:i+len(old)] == old:
        result += new
        i += len(old)
    else:
        result += text[i]
        i += 1

print(result)


a = 5
b = 3
operation = "add"

if operation == "add":
    result = a + b
elif operation == "subtract":
    result = a - b
elif operation == "multiply":
    result = a * b
elif operation == "divide":
    if b != 0:
        result = a / b
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

print(result)