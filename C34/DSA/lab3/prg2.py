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
            print("Invalid word")
        else  :  
            print("Valid Word!" )
    
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
    T[pos].search(st)

if __name__ == '__main__':
    main()


