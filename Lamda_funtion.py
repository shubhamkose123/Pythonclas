x= lambda x : x**2
y= lambda x : x+10
print(x(5))
print(y(5))

a = lambda x,y,z,p,q,r: x+y-z/p%q//r
print(a(1,2,3,4,5,6))

my_list=[10,15,20,25,30,35,40,45,50]
x= list(filter(lambda x: x%2==0,my_list))
print(x)


from functools import reduce
my_list=[10,15,20,25,30,35,40,45,50]
x= (filter(lambda x: x%2==0,my_list))
y= reduce(lambda x,y:x+y,x)
print(y)




my_list=[10,15,20,25,30,35,40,45,50]
even_data=list(filter(lambda x: x%2==0,my_list))
squer_even=list(map(lambda x: x**2,even_data))
squer_sum=reduce(lambda x,y:x+y,squer_even)
print(even_data)
print(squer_even)
print(squer_sum)