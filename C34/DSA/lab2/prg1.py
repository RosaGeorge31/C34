class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()

    def insert(self,x,p):
        """Insert element x in the position after p"""
        pos = p
        temp = ListNode()
        temp.value = x
        
        temp.next = pos.next
        pos.next = temp    

    def delete(self,p):
        """Delete the node following node p in the linked list."""
        temp = p.next
        p.next = temp.next

    def printList(self):
        """ Print all the elements of a list in a row."""
        ptr = self.head
        ptr = ptr.next
        print("\nList is :")
        while ptr!=None:
			
            print(str(ptr.value), end = ' , ')
            ptr = ptr.next
        print("")
       

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp = ListNode()
        temp.value = x
        
        ptr = self.head
        ct = 0
        while ptr!=None:
            if ct == i:
                break
            ct = ct + 1
            ptr = ptr.next
        
        temp.next = ptr.next
        ptr.next = temp    
        

    def search(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        ptr = self.head
        while ptr!=None:
            if ptr.value==x:
                return ptr
            ptr = ptr.next
        return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        ptr = self.head
        ct = 0
        while ptr!=None:
            ct = ct + 1
            ptr = ptr.next        
        ct = ct - 1
        return ct

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.head.next == None:
            return True
        else : 
            return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self):
        self.value=0
        self.next=None

def main():
    L = LinkedList()
    L.insert(10,L.head)
    L.printList()
    L.insert(12,L.head.next)
    L.printList()
    L.insert(2,L.head)   
    L.printList()
    print('Size of L is ',L.len())
    L.delete(L.head)
    L.printList()
    L.delete(L.head.next)
    L.printList()
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertval(2,0)
    L.insertval(1,0)
    L.insertval(4,2)
    L.insertval(3,2)
    L.printList()
    ch = int(input("\nEnter a number"))
    pt = L.search(ch)
    if pt!=None:
        ptr=L.head
        c=0
        while ptr!=pt:
            c=c+1
            ptr = ptr.next
        print("\nValue " + str(pt.value) + " is found at position " + str(c))
    else: 
        print("Value " + str(4) + " not found")
   
if __name__ == '__main__':
    main()
