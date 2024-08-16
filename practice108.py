count=int(input("How many students: "))
fileout=open("Marks.txt","w")
for i in range(count):
    print("Enter details for student",(i+1),"below:")
    Roll_no=int(input("Enter roll no: "))
    Name=input("Enter name: ")
    Marks=int(input("Enter marks: "))
    rec=str(Roll_no)+','+Name+','+str(Marks)+'\n'
    fileout.write(rec)
fileout.close()

