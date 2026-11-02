#  practic-1

# def welcome(name):
#   message = "Welcome: " + name
#   return message
# print(welcome("Dana"))
# print(welcome("Avi"))

# #  practic-2

# x = "global"
# def first():
#  x = "local in first"
#  print("1:", x)
# def second():
#  print("2:", x)
# first()
# second()
# print("3:", x)

#  practic-3

# count = 0
# def add_one(count):
#  count = count + 1
# add_one(count)


#  practic-4

list = [1, 2, 3]
numbers = list(range(5)) #TypeError בגלל שהוא לא מצא את הפונקציה listמכיוון שהיא תפוסה במשתנה

#  practic-5
cart = []
total = 0
def add(price):
    total = 0
    lst =[]
    lst.append(price)
    total = total + price
    return lst
add(100)
add(50)
print(cart,total)