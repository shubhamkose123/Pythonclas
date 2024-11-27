#index
#  index , index(element,start,end)
# nums = [2,43,45,56,7,8,9,-33,44,45,5,6,45,5,6]
# a=nums.index(45,10)
# print(a)
#====================================
# nums = [2,43,45,56,7,8,9,-33,44,45,5,6,45,5,6]
# a=nums.index(45,0)
# print(a)
# b=nums.index(45,a+1)

# print(b)
# c=nums.index(45,b+1)
# print(c)

# print("45:-",a,b,c,)
#=======================================================================
#index()return index value of element passsed,
#we can give maximum of 3 paramitar in index()
#in frist paramitar , u have to pass the elmet 
#itself
#and second and thried are optional perametaor,
#second-->start
#third---> end(exclude)
#if element is not found it thorow an exception
#=====================================================
#  count() --->return frequency
# nums = [2,43,45,56,7,8,9,-33,44,45,5,6,45,5,6]
# a=nums.count(2)
# print(a)
#===================sort===========================
#inplace function
#no need of extra list(opject)
#note:- 
nums = [2,43,45,56,7,8,9,-33,44,45,5,6,45,5,6]
nums.sort()
print(nums)


