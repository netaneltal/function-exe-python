# practic-1

# def apply_to_all(numbers,action):
#     nums = []
#     for n in numbers:
#         nums.append(action(n))
#     return nums

# def double(n):
#     return n * 2

# def rounde(n):
#     return round(n)
    
# print(apply_to_all([1,2,3],double))    
# print(apply_to_all([1,2,3],lambda n: n * n))
# print(apply_to_all([1.4,2.6,3.8],rounde)) 

# practic-2

# prices = [20,75,120,45,90]

# expensive = list(filter(lambda p: p>50,prices))
# raised = list(map(lambda p: p+10,expensive))
# print(expensive)
# print(raised)

# practic-3

# words = ["banana", "fig", "cherry", "kiwi"]

# print(sorted(words,key = len))
# print(max(words,key = len))

# students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]

# for name, grade in sorted(students, key=lambda s: s[1],reverse= True):
#     print(name)

# practic-4

# def make_discount(percent):
#     def discount(price):
#           price =price-(price* percent / 100)
         
#           return price
#     return discount

# ten_off = make_discount(10)
# half_price = make_discount(50)
# print(ten_off(200))
# print(half_price(200))


# practic-5

# def apply_to_all(numbers,action):
#   lst = []
#   for n in numbers:
#     lst.append(action(n))
#   return lst


# def double(n):
#   return n * 2

# print(apply_to_all([1, 2], double)) 
