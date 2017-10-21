class TreeNode:
    def __init__(self):
        self.parent= None
        self.left = None
        self.right = None
        self.val = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = TreeNode()
        
                
    def insertLeft(self,x,key):
        if self.root.val == None:  
            self.root.val = key
            return
        
        temp = TreeNode()
        temp.val = key
        par = self.root.parent
        ptr = self.root
        while ptr is not None:
            par = ptr
            f = 0
            if key <= ptr.val:
                ptr = ptr.left
                f=1
            else:
                ptr = ptr.right
                
        if f ==1:
            par.left = temp
            temp.parent = par
        else:
            par.right = temp
            temp.parent = par


     def insertRight(self,key):
        if self.root.val == None:  
            self.root.val = key
            return
        
        temp = TreeNode()
        temp.val = key
        par = self.root.parent
        ptr = self.root
        while ptr is not None:
            par = ptr
            f = 0
            if key <= ptr.val:
                ptr = ptr.left
                f=1
            else:
                ptr = ptr.right
                
        if f ==1:
            par.left = temp
            temp.parent = par
        else:
            par.right = temp
            temp.parent = par
                
    def delete(self,v):
        pos = self.search(self.root,v)
        
        if pos.left is None and pos.right is None:
            print("in")
            if pos.parent.val > pos.val:
                pos.parent.left = None
            else:
                pos.parent.right = None
            return
        if pos.left is None :
            if pos.parent.left == pos:
                pos.parent.left = pos.right
            else:
                pos.parent.right = pos.right
            return
               
        if pos.right is None :
            if pos.parent.left == pos:
                pos.parent.left = pos.left
            else:
                pos.parent.right = pos.left
            return
        y = self.predecessor(self.root,v)
        pos.val = y.val
        if y.left is None and y.right is None:
            if y.parent.left == y:
                y.parent.left = None
            else:
                y.parent.right = None
            return
        if y.left is None :
            if y.parent.left == y:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            return
               
        if y.right is None :
            if y.parent.left == y:
                y.parent.left = y.left
            else:
                y.parent.right = y.left
            return
            
    def display(self,x):
        if x == None:
            return
        else:
            print (x.val, end ='  ')
            self.display(x.left)
            self.display(x.right)
            
        
def main():
    T = BinarySearchTree()
    T.insert(5)
    T.insert(3)
    T.insert(9)
    T.insert(1)
    T.insert(8)
    T.insert(4)
    T.display(T.root)
    print('')
    print("max : " + str(T.maximum(T.root).val))
    print("min : " + str(T.minimum(T.root).val))
    s = int(input("Enter the value to be searched for : "))
    if T.search(T.root,s) == None:
        print("Element not found!!")
    else:
        print("Element found!")
    s = int(input("Enter a value  "))
    a = T.predecessor(T.root,s)
    if a is not None:
        print("pre : " + str(a.val))
    else:
        print("Pre : " + str(a))
    
    a = T.successor(T.root,s)
    if a is not None:
        print("post : " + str(a.val))
    else:   
        print("Post : " + str(a))
    T.delete(4)
    T.delete(5)
    print("root : " + str(T.root.val))
    T.display(T.root)
    print('')
if __name__=='__main__':
    main()      
        
        
                       
                      
            
