# def show(**kwargs):
#     print(kwargs)
#     for i,j in kwargs.items():
#         print(i,"=",j)
# show (name ='Shubham' , age=24 , qeali = 'M.tech')        
# ============================================================
#                         Scope:-
# x=10
# def show():
#     global y
#     y=20
#     print(x)
#     print(y)
# show()
# print(x)
# print(y)
# ====================================
x=10
def show():
    global y
    x=50
    y=30
    print(globals()['x'])
show()
print(x)
print(y)   

