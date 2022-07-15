
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

def searchBST(root,key):
    if root is None:
        return None
    else:
        if root.val==key:
            return root
        elif root.val<key:
            return searchBST(root.right,key)
        else:
            return searchBST(root.left,key)    
    

if __name__=="__main__":
    root=binaryTree(int(input("Enter Root node value: ")))
    # root=None
    n=int(input("Enter no. of elements to enter in BST: "))
    print("Insert the Elements: ")
    for i in range(0,n):
        root=insertIntoBST(root,int(input()))  
        
    print("Printing BST via Inorder traversal: ")     
    printBST(root)  
    n=int(input("Enter an element to search: "))
    if(searchBST(root,n)is not None):
        print("Element found.")
    else:
        print("Element does not exist!!")    
      