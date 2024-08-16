def interest(p,r=0.10,t=2):
    return (p*r*t)/100
prin=float(input("Enter principal value: "))
print("The simple interest with default rate and time values: ",interest(prin))
roi=float(input("Enter rate of interest: "))
time=int(input("Enter time in years: "))
print("The simple interest with provided rate and time values: ",interest(prin,roi/100,time))
