def create_user():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    born_year = input("Enter year of birth: ")
    password = input("Enter password: ")
    email = input("Enter email (optional): ")

    if name:
        print("Name: ", name)
    else:
        print("Name not provided")

    if surname:
        print("Surname: ", surname)
    else:
        print("Surname not provided")

    if born_year:
        print("Born Year: ", born_year)
    else:
        print("Born Year not provided")

    if password:
        print("Password: ", password)
    else:
        print("Password not provided")

    if email:
        print("Email: ", email)
    else:
        print("Email not provided")

create_user()