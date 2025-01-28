def manual_difference(set1, set2):
    for i in list(set1):
        if i in set2:
            set1.remove(i)
    return set1

student_1 = {
    "name": "Nikoloz",
    "surname": "Antadze",
    "age": 14,
    "average_score": 100
}

student_2 = {
    "name": "Luka",
    "surname": "Suranishvili",
    "age": 15,
    "average_score": 100
}

print(student_1)
print(student_2)