def interest(principal,rate=0.10,time=2):
     return principal*rate*time
prin=float(input("Enter the principal amount: "))
b=interest(prin)
print("Rs. ",b)
roi=float(input("Enter the rate of interest: "))
time=float(input("Enter the time: "))
c=interest(prin,roi/100,time)
print("Rs. ",c)
