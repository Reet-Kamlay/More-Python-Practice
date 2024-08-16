def interest(principal,time=2,rate=0.10):
    return principal*time*rate
prin=float(input("Enter the principal amount: "))
a=interest(prin)
print("Rs. ",a)
roi=float(input("Enter the rate of interest: "))
time=float(input("Enter the time: "))
b=interest(prin,roi/100,time)
print("Rs. ",b)
