n=int(input("How many students: "))
compWinners={}
for a in range(n):
    key=input("Name of the student: ")
    value=int(input("Number of competitions won: "))
    compWinners[key]=value
print("The dictionary now is:")
print(compWinners)
