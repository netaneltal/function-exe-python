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

# list = [1, 2, 3]
# numbers = list(range(5)) #TypeError בגלל שהוא לא מצא את הפונקציה listמכיוון שהיא תפוסה במשתנה

#  practic-5

def add(cart,price):
    return cart + [price]
def cart_total(cart):
    return sum(cart)
   
cart = []
cart = add(cart, 100)
cart = add(cart, 50)
print(cart,cart_total(cart))
print(cart)