# fruit = ("apple",20,100)
# print(type(fruit))
# #fruit[2]=200 #tuple immutable
# print(id(fruit))
# print(id(fruit[0]),id(fruit[1]),id(fruit[2]))

# fruit = ("apple",20,100)
# fruit = ("apple",20,100) + ("bnaana",200)
# print(type(fruit))
# print(fruit)

# mytuple = ("apple", "banana", "cherry")
# print(mytuple)

# thistuple = ("apple",)
# print(type(thistuple))
#============================================
#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
# ===============================
# number = (12,99) + (78,90)
# number = number + (89,90)
# print(number)
# ======================================
# lis = [["ajay","aman"],(45,67)]
# lis.pop()
# print(lis)
# print(type(lis[1]))
#lis[1][0]=99  =error (tuple)

# ================================
# t = (34,55,[3,4,555])
# t[1][2]=9999
# print(t)
# ====================================
# lis = [["ajay","aman"],(45,[67,44])]
# lis[1][1][0]=5555555
# print(lis)
# ============================
# lis = [["ajay","aman"],(45,[67,44],[54,62])]
# lis[1][2][0]=44444
# print(lis)
# ========================================================
# t = (54,62,58,9)
# a=t.count(9)
# print(a)
# # ==========================
# t = (9,44,5,3,9)
# a=sorted(t)
# print(a)
# ======================(singlae h int)==============================
t = (23)
print(type(t))
#==========================
t=(23,)
print(type(t))
#==========================
t1 = ("a,b,c,d",)
print(type(t1))
# ====================
t2 = 1,2,3,4,5       #function
print(type(t2))
# ===============empty(tuple)==============================
t = ()
t1 = tuple()
print(t,t1)
# ==================
record = ("shubham",252,54,6265702646)
print(record)
record= list(record)
record[3],record[0]=7863927787,"shubham kose"
print(record)
record = tuple(record)
print(record)
# ==========================
