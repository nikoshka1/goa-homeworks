set_1 = {1, 2, 3, 4, 5}
set_1.add(6)
set_1.remove(3)
set_1.clear()
removed_element = set_1.pop()
set_2 = set_1.copy()
other_set = {8, 9, 10}
difference = set_1.difference(other_set)
print(set_1)
print(removed_element)
print(difference)

my_dict = {
    "name": "John",
    "last_name": "Doe",
    "age": 30
}
print(my_dict.keys())
print(my_dict.values())

def addtodatabase(first_name, last_name, age):
    person_data = {
        "Nikoloz": first_name,
        "Antadze": last_name,
        "14": age
    }
    return person_data

database_entry = addtodatabase("John", "Doe", 30)
print(database_entry)