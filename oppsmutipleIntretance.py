'''
Same Name Function With Diffarent Orgimain
Type:-
     1)Method Overloading
     2)Method Overolirg
'''
# class father:
#     x=10
#     y=20
#     z=30
#     def property(self):
#         self.name= 'f_name'
#         self.bank= 'f_bank'
#         print(self.name)
#         print(self.bank)  
# class mother:
#     p=19 
#     o=32
#     i=89
#     def property1(self):
#         self.name1= 'm_name'
#         self.bank2= 'm_bank'
#         print(self.name1)
#         print(self.bank2)
# class son(father, mother):
#     pass
# # print(dir(son))
# obj=son()
# obj.property()
# obj.property1()

class A:
    def add(self,*n):
        sum=0
        for i in n:
            sum=sum+i
        return sum
obj=A()
x=obj.add(10,20)
print(x)
y=obj.add(10,20,30)
print(y)

   


