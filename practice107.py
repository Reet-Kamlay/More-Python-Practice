fileout=open("Marks.txt","a")
for i in range(2):
    print("Enter details for student",(i+1),"below")
    Roll_no=int(input("Enter roll no: "))
    Name=input("Enter name: ")
    Marks=int(input("Enter roll no: "))
    rec=str(Roll_no)+','+Name+','+str(Marks)+'\n'
    fileout.write(rec)
fileout.close()
    
