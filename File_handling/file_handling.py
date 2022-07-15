import os


f=open("test_file.csv","r")
f1=open("test_file(1).csv","w")
f.seek(0)
f1.write(f.readline())
for x in f:
    x=str(x).split(",")
    x[3]=str(int(x[3])+1)+"\n"
    x=",".join(x)
    #print(x)
    f1.write(x)
else:
    print("Succesfully Updated")    
f.close() 
f1.close()  

os.remove("test_file.csv")
os.rename("test_file(1).csv","test_file.csv")