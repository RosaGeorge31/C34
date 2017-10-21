class TreeNode:
    def __init__(self):
        self.parent= None
        self.left = None
        self.right = None
        self.val = None
        self.ht = 1        

class AVLTree:
    def __init__(self):
        self.root = TreeNode()
          
               
    def insert(self,key):
        
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
            
        self.inc_ht(temp)
                
        ptr = par
        z = None

        while ptr is not None:
                            
            if ptr.left is None:
                diff = ptr.right.ht 
                if diff >= 2:
                    z = ptr                    
                    break
            elif ptr.right is None:
                diff = ptr.left.ht 
                if diff >= 2:
                    z = ptr
                    break
            else:
                diff = abs( ptr.left.ht - ptr.right.ht )
                if diff >= 2:
                   z = ptr
                   break
            ptr = ptr.parent
        
        if z is None:
            return
        print("z is : " +str(z.val))
        
        prpr = temp
        pr = temp.parent
        ptr = temp.parent.parent
        
        while ptr is not z :
            prpr = pr
            pr = ptr
            ptr = ptr.parent
        
        x = prpr
        y = pr
        
        print("y is : " +str(y.val))
        print("x is : " +str(x.val))
        
        if z.left is y and y.left is x:
            if z.parent is None: #root
                print("CASE 1 a")
                self.root = y
                z.left = y.right
                z.parent = y
                y.right = z
                y.parent = None
                y.ht = x.ht + 1             
                z.ht = x.ht
                self.inc_ht(z)
                return
            else:
                print("CASE 1 b")
                pt = z.parent
                y.parent = pt
                pt.left = y
                z.left = y.right
                z.parent = y
                y.right = z
                
                y.ht = x.ht + 1             
                z.ht = x.ht
                self.inc_ht(z)
                return

        elif z.right is y and y.right is x:
            if z.parent is None: #root
                print("CASE 2 a")
                self.root = y
                z.right = y.left
                z.parent = y
                y.left = z
                y.parent = None
                y.ht = x.ht + 1             
                z.ht = x.ht
                self.inc_ht(z)
                return
            else:
                print("CASE 2 b")
                pt = z.parent
                y.parent = pt
                pt.right = y
                z.right = y.left
                z.parent = y
                y.left = z
                y.ht = x.ht + 1             
                z.ht = x.ht
                self.inc_ht(z)
                return

        elif z.left is y and y.right is x:
                              
                pt = z.parent
                if pt is None:
                    print("CASE 3 a")
                    z.left = x
                    x.parent = z
                    x.left = y
                    y.right = x.left
                    y.parent = x
                
                    y.ht = x.ht
                    x.ht = y.ht + 1
                    
    
                    z.left = x.right
                    z.parent = x
                    x.right = z
                    x.parent = pt
                    self.root = x
                    x.ht = y.ht + 1             
                    z.ht = y.ht   
                    self.inc_ht(x)
                else:
                    print("CASE 3 b")
                    z.left = x
                    x.parent = z
                    x.left = y
                    y.right = x.left
                    y.parent = x
                
                    y.ht = x.ht
                    x.ht = y.ht + 1
                    self.inc_ht(y)
    
                    z.left = x.right
                    z.parent = x
                    x.right = z
                    x.parent = pt
                    pt.left = x
                    x.ht = y.ht + 1             
                    z.ht = y.ht   
                    self.inc_ht(x)
        else:
                print("CASE 4")
                pt = z.parent

                z.right = x
                x.parent = z
                y.left = x.right
                y.parent = x
                x.right = y
                y.ht = x.ht
                x.ht = y.ht + 1


                z.right = x.left
                z.parent = x
                x.left = z
                x.parent = pt
                x.ht = y.ht + 1             
                z.ht = y.ht            


     
    def inc_ht(self,v):
        ptr = v.parent
        while ptr is not None:
            if ptr.left is None:
                ptr.ht = ptr.right.ht +1
            elif ptr.right is None:
                ptr.ht = ptr.left.ht +1
            else:
                ptr.ht = max(ptr.left.ht,ptr.right.ht) + 1
            ptr = ptr.parent
            
    def display(self,x):
        if x == None:
            return
        else:
            print(str(x.val) + " ht: " + str(x.ht))
            self.display(x.left)
            self.display(x.right)
          
def main():
    T = AVLTree()
    T.insert(10)
    T.display(T.root)
    print('')
    T.insert(12)
    T.display(T.root)
    print('')
   
    T.insert(8)
    T.display(T.root)
    print('')
    T.insert(14)
    T.display(T.root)
    print('')
    T.insert(16)
    T.display(T.root)
    print('')
    T.insert(13)
    T.display(T.root)
    print('')
    print('root : ' + str(T.root.val))
    
    
    
if __name__=='__main__':
    main()      
        
        
                       
                      
            
