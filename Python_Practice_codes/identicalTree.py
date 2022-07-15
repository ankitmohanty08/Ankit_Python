
class binaryTree:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
 
def insertIntoBST(root,key):
     if root is None:
         return binaryTree(key)  
     else:
         if root.val ==key:
             return root
         elif root.val<key:
             root.right=insertIntoBST(root.right,key)     
         else:
             root.left=insertIntoBST(root.left,key) 
     return root


def printBST(root):
    #print inOrder -> (left)->(root)->(right)
    if root is not None:
        printBST(root.left)            
        print(root.val)
        printBST(root.right)

def checkIdentical(root1,root2):
    if root1==None and root2==None:
        return True
    elif root1!=None and root2!=None:
        if root1.val==root2.val:
            if(checkIdentical(root1.left,root2.left)):
                return checkIdentical(root1.right,root2.right)
            else:
                return False
        else:
            return False    
    else:
        return False

if __name__=="__main__":
    
    # Inserting Tree 1
    
    root1=binaryTree(int(input("Enter Root node value for Tree 1: ")))
    n=int(input("Enter no. of elements to enter in Tree 1: "))
    print("Insert the Elements: ")
    for i in range(0,n):
        root1=insertIntoBST(root1,int(input()))  
        
    print("Printing BST via Inorder traversal: ")     
    printBST(root1)  
    
    # Inserting Tree 2
    
    root2=binaryTree(int(input("Enter Root node value for Tree 2: ")))
    n=int(input("Enter no. of elements to enter in Tree 2: "))
    print("Insert the Elements: ")
    for i in range(0,n):
        root2=insertIntoBST(root2,int(input()))  
        
    print("Printing BST via Inorder traversal: ")     
    printBST(root2)  
    
    if(checkIdentical(root1,root2)):
        print("They are Identical")
    else:
        print("They are not Identical")
    
      