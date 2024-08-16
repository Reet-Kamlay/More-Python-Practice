line=input("Enter a line: ")
lowercount=uppercount=0
digitcount=alphacount=0
for a in line:
    if a.islower:
        lowercount+=1
    elif a.isupper:
        uppercount+=1
    elif a.isdigit:
        digitcount+=1
    if a.isalpha:
        alphacount+=1
print("no of alphabets:",alphacount)
print("no of uppercase letters:",uppercount)
print("no of lowercase letters:",lowercount)
print("no of digits:",digitcount)
