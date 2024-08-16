AM=int(input("Enter Average marks: "))
if AM>=90:
    print("A+")
elif AM>=80 and AM<90:
    print("A")
elif AM>=70 and AM<80:
    print("B")
elif AM>=60 and AM<70:
    print("C")
elif AM>=50 and AM<60:
    print("D")
elif AM>=33 and AM<50:
    print("E")
else:
    print("F")
