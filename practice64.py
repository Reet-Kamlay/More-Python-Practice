avg=int(input("Enter your average marks: "))
if avg<=40:
    print("Your grade is F")
elif avg>40 and avg<50:
    print("Your grade is E")
elif avg>50 and avg<60:
    print("Your grade is D")
elif avg>60 and avg<75:
    print("Your grade is C")
elif avg>75 and avg<85:
    print("Your grade is B")
elif avg>85 and avg<95:
    print("Your grade is A")
elif avg>95 and avg<100:
    print("Your grade is A+")
else:
    print("Invalid marks")
