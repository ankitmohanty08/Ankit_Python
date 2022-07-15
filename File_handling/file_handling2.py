test_contents=[]
f=open("test_file.csv","r+")
keys=str(f.readline()).split(",")
#print(keys)

for data in f:
    data=str(data).strip().split(",")
    data[3]=str(int(data[3])+1)+"\n"
    #print(data)
    dict={}
    for i in range(0,4):
        dict[keys[i]]=data[i]
    test_contents.append(dict)
       
#print(test_contents)
f.seek(0)
headerList=list(test_contents[0].keys())
headers=",".join(headerList)
f.write(headers)
for dict in test_contents:
    valueList=list(dict.values())
    value=",".join(valueList)
    f.write(value)

f.close()

