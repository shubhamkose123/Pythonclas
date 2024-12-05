# n=int(input("Enter any no "))
# i=1
# while i<=n:
#     if i==5:
#         i=i+1
#         continue
#     else:
#         print(i)
#         i=i+1
#    ===============================================
# n=int(input("Enter any no "))
# i=1
# while i<=n:
#     if i==5:
#         pass
#         i=i+1
#     else:
#         print(i)
#         i=i+1
# ====================================================
while True:
    print("1.Add\n,2.Sub\n,3.Div\n,4.Mul\n,5.off")
    n=int(input("Enter your Choise="))
    x=[1,2,3,4,5]
    if n in x:
        x=int(input("Enter 1St number="))
        y=int(input("Enter 2nd number="))
        if n==1:
            print("Addition=",x+y)
        elif n==2:
            print("Sub=",x-y)    
        elif n==3:
            print("Div=",x/y)        
        elif n==4:
            print("Mul=",x*y)    
    elif n==5:
        break 
    else:
        print("you enterd wrong no")
  

        

        
