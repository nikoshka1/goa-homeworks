def high_and_low(_str):
    res = _str.split(" ")
    _arr = []
    for elem in res:
        _arr.append(int(elem))
    return f"{ min(_arr) } { max(_arr) }"

print(high_and_low("1 22 44 55 123"))
print(high_and_low("123 345 6543"))