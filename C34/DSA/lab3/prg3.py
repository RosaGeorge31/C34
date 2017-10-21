class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()

    
    def search(self,x):
        #Search for key x in the list. Return a reference to the first node with key x; return None if no such node is found.
        ptr = self.head
        while ptr!=None:
            if ptr.key==x:
               return ptr
            ptr = ptr.next
        return None

class Hashtable:
    def printList(self):
        """ Print all the elements of a list in a row."""
        ptr = self.L.head
        
        print("\nList is :")
        while ptr.next!=None:
            print(str(ptr.key), end = ' , ')
            ptr = ptr.next
        print("")
        
    def __init__(self):
       self.L = LinkedList()
       
    def insert(self, k):
        if self.L.head==None:   
            temp =  ListNode()
            temp.key = k
            temp.next = None
            self.L.head = temp
        else :
            temp = ListNode()
            temp.key = k
            temp.next = self.L.head
            self.L.head = temp
        
    def search(self,k):
        if self.L.search(k) == None:
            return False
        else:  
            return True
    
    def allkeys(self):
        Keys = []
        ptr = self.L.head
        
        while ptr.next!=None:
            Keys.append(ptr.key)    
            ptr = ptr.next
        return Keys   
class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: key, next. 
    """
    def __init__(self):
        self.key=None
        self.next=None

def main():
    T = [None for i in range(30)]
    
    for i in range(30):
        T[i] = Hashtable()
    with open("ispell.dict", "r") as ins:
        array = []
        for line in ins:
            s = line.split()
            array.append(s[0])
   
    for i in range(len(array)):
        s = str(array[i])
        val=0
        for j in range(len(s)):
             val=33*val+ord(s[j])

        pos=val%30	
        T[pos].insert(s)
        
      
    st = input("Enter a string: \n");
    st = st.lower()
    tot = 0
    val=0
    for i in range(len(st)):
        val=33*val+ord(st[i])

    pos=val%30	
    if T[pos].search(st)==True:
        print("Valid word!")
    else:
        words = []         
        for j in range(97,123):
            for i in range(len(st)):
                t = st[:i]
           
                c = (chr(j))
                t= t+c
                t = t + st[i+1:]
                val=0
                for k in range(len(t)):
                     val=33*val+ord(t[k])

                pos=val%30	
                if T[pos].search(t)==True:
                          
                    if t not in words:
                        words.append(t)
                    else:
                        break

                    
                   
        print("The list : ")
        for i in words:
            print(i, end = ' , ') 
        print('')    
			

if __name__ == '__main__':
    main()


