# def nugzar_chubinidze(sadgerdzelo, limit):
#     if type(sadgerdzelo) == str or type(limit) == str:
#         return None
#     elif sadgerdzelo > limit:
#         return "ნუგზარი აღარ დალიო მეტი!"
#     else:
#         return "მოდი ახლა მართლა, დამილოცნიე!" 
    
# print(nugzar_chubinidze("asd",2))

# def Yuri(tsneva, pulsi):
#     Yuris_tsneva = 120
#     Yuris_pulsi = 80
#     if tsneva == Yuris_tsneva and pulsi == Yuris_pulsi:
#         return True
#     else:
#         return False
    
# print(Yuri(120,80))

# def captianjack(gold_coin):
#     if gold_coin == 0:
#         return print("Puli moitane")
#     print("Aba airche oyond uyure puli unda geyos")
#     print("Gemi 1: 150 maneti")
#     print("Gemi 2: 200 maneti")
#     print("Gemi 3: 250 maneti")
#     print("Gemi 4: 300 maneti")
#     print("Gemi 5: 350 maneti")
#     archeva = input("Aba romeli airchie? ")
#     if archeva == 1:
#         if gold_coin >= 150:
#             print("Mshvidobashi!")
#         else:
#             print("Puli ar gyopnis")
#     elif archeva == 2:
#         if gold_coin >= 200:
#             print("Mshvidobashi!")
#         else:
#             print("Puli ar gyopnis")
#     elif archeva == "3":
#         if gold_coin >= 250:
#             print("Mshvidobashi")
#         else:
#             print("Puli ar gyopnis")
#     elif archeva == "4":
#         if gold_coin >= 300:
#             print("Mshvidobashi")
#         else:
#             print("Puli ar gyopnis")
#     elif archeva == "5":
#         if gold_coin >= 350:
#             gold_coin -= 350
#             print("Mshvidobashi")
#         else:
#             print("Puli ar gyopnis")
#     else:
#         print("Wadi gaiare")

# captianjack(1000)

def vashlebi(vashlebis_saxelebi):
    seti = set(vashlebis_saxelebi)
    return seti

arr = ["a", "a", "a", "b","b"]

print(vashlebi(arr))