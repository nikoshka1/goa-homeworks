elements = []

for i in range(4):
    elements += input("გთხოვთ, შეიყვანოთ ელემენტი: ")

print(elements)

sia = [9,5,94,711,52,96,71,8]
smallest = sia[0]

for i in range(len(sia)):
    if sia[i] < smallest:
        smallest = sia[i]

print(smallest)
