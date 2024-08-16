m1=int(input("Enter your Subject Marks 1:"))
m2=int(input("Enter your Subject Marks 2:"))
m3=int(input("Enter your Subject Marks 3:"))
t=m1+m2+m3
if m1>=33:
    if m2>=33:
        if m3>=33:
            print("Pass")
        else:
            print("Fail 3")
    else:
        print("Fail 2")
else:
    print("Fail 1")
            
    
