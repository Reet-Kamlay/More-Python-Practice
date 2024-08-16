line=input("Enter a line:")
uppercount=lowercount=0
digitcount=alphacount=0
for a in line:
    if a.isupper():
        uppercount+=1
    if a.isalpha():
        alphacount+=1
    elif a.isdigit():
        digitcount+=1
    elif a.islower():
        lowercount+=1
print("No of lowercase letters:",lowercount)
print("No of uppercase letters:",uppercount)
print("No of alphacase letters:",alphacount)
print("No of digitcase letters:",digitcount)
        
