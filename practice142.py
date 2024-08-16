def simple_interest(prin,rate=5.4,time=10):
    return (prin*rate*time)/100
prin=float(input("Enter principal amount: "))
si=simple_interest(prin)
print("Simple interest=",si)
