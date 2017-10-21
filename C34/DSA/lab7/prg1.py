class node:
    def __init__(self):
        self.L = [None for i in range(26)]
        self.parent = None
        self.nodes = [None for i in range(26)]
        

class Trie:
    
    def __init__(self):
        self.root = None

    def insert(self,val):
        
        if self.root is None:
           n = node()
           self.root = n
           index = ord(val[0])-97
           print("inserted: " + str(val[0]))  
           self.root.L[index] = val[0] 
           c = 1
           val = val[1:]
           for i in val:
               
               newnode = node()
               newnode.L[ord(i) - 97] = i
               newnode.parent = n
               print("inserted: " + str(i))  
               n.nodes[index] = newnode
               n = newnode
               if c == len(val):
                              
                   return
               else:
                   index = ord(val[c])-97
                   c+=1
                         

        else:
            print("in 2")
            index = ord(val[0])-97
            if self.root.L[index] is None:
                n = node()
                self.root.L[index] = val[0]  
                print("inserted: " + str(val[0]))                             
                val = val[1:]
                c=1
                for i in val:
                    newnode = node()
                    newnode.L[ord(i) - 97] = i
                    print("inserted: " + str(i))
                    newnode.parent = n
                    n.nodes[index] = newnode
                    n = newnode   
                    if c == len(val):
                       return
                    else:
                       index = ord(val[c])-97
                       c+=1
            else:
                print("in 3")
                n = self.root
                c = 0
                while n.L[index] == val[c]:
                    prev = n
                    n = n.nodes[index]
                    c = c + 1
                    if n is None:
                        break
                    if val[c] is None:
                        return
                    index = ord(val[c])-97                    
                
                n = prev
                index = ord(val[c])-97 
                
                s = val[c:]
                l = len(s)
                c = 0
                
                for i in s:
                    newnode = node()
                    newnode.L[ord(i) - 97] = i
                    print("inserted: " + str(newnode.L[ord(i) - 97]))
                    newnode.parent = n
                    n.nodes[index] = newnode
                    n = newnode  
                    if c == l-1:
                       return
                    else:
                        index = ord(s[c])-97
                        c+=1


                   
              
           
def main():
    T = Trie()
    T.insert("happy")
    T.insert("handy")
    T.insert("rosa")
    T.insert("rosita")
if __name__=='__main__':
    main()

