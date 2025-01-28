def binary(a):
    answer = ""
    while a > 0:
        answer = str(a % 2) + answer
        a = a//2
    return answer
print(binary(14))