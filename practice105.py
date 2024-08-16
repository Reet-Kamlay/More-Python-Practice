myfile=open(".txt","r")
ch=" "
vcount=0
ccount=0
while ch:
    if ch in ['a','A','e','E','i','I','o','O','u','U']:
        vcount+=1
    else:
        ccount+=1
print("Vowels in the file:",vcount)
print("Consonants in the file:",ccount)
myfile.close()
