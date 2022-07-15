


def insertArray():
    n=int(input("Enter no. of elemnets to insert: "))
    arr=[]
    for i in range(0,n):
        x=int(input())
        arr.append(x)
    return arr

def reverseArray(arr,index):
    '''
    arguments- arr (list)
              index- index to swap   
    '''
    length=len(arr)
    if(index==length//2): #if index == middle element then return
        return 
    else:
        #Swapping index and length-1-index elements
        temp=arr[index]
        arr[index]=arr[length-1-index]
        arr[length-1-index]=temp
        #incrementing index by 1 
        reverseArray(arr,index+1)
           

if __name__=="__main__":
    arr=insertArray()
    print("Array before reversing: ",arr)
    reverseArray(arr,0)
    print("Array after reversing: ",arr)
    
