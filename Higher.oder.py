#map:-
# my_list=[10,20,30,40,50]
# def dic(x):
#     return x-5
# x=map(dic,my_list)
# print(tuple(x))
# ================================
# my_list=[10,20,30,40,50]
# def dic(x):
#     return x**2
# x=map(dic,my_list)
# print(tuple(x))
# ===================================
# filter():-
# my_tuple=(70,75,60,59,40,60,80)
# def grater_60(x):
#     if x>60:
#         return x
# x=tuple(filter(grater_60,my_tuple))
# print(x)  
# ========================================
# Reduce()
from functools import reduce
my_tuple=(10,20,30,60,40,50)
def my_digit(x,y):
    if x>y:
        return x
    else:
        return y
x=reduce(my_digit,my_tuple)
print(x)    
        
  

