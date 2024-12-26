'''
In Python, encapsulation is an object-oriented programming (OOP) 
principle that combines data and methods into a single unit called a class.
 This concept helps to hide the internal state of an object from the outside world.
           access specifiens
                  |
                  |__public    (Govt.place)
                  |__protected (over-capus)
                  |__private   (private-house)      
'''
class A:
    __x=10
    def __show(self):
        print("from class A")
class B (A):
    pass
print(dir(B))
obj=B()
obj._A__show()
     