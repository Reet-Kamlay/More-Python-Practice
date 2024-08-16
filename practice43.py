m1=int(input("Enter your Subject Marks 1:"))
m2=int(input("Enter your Subject Marks 2:"))
m3=int(input("Enter your Subject Marks 3:"))
t=m1+m2+m3
if m1>=33 and m2>=33 and m3>=33:
    print("pass in all subjects")
else:
    if m1<33:
        print("Fail in 1")
    elif m2<33:
        print("Fail in 2")
    elif m3<33:
        print("Fail in 3")
