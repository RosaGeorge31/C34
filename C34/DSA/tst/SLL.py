class LinkedList:
	def __init__(self):
		self.head=Node()

	def insert(self,k,pos):
		temp=Node()
		temp.val=k
		temp.next=pos.next
		pos.next=temp

	def delete(self,pos):
		temp=pos.val		
		pos.next=pos.next.next
		return temp

	def insertval(self,k,i):
		ptr=self.head
		temp=Node()
		temp.val=k
		c=0
		while ptr!=None:
			if(c==(i)):
				break			
			ptr = ptr.next
			c=c+1

		temp.next=ptr.next
		ptr.next=temp

	def deleteval(self,i):
		ptr=self.head
		c=0
		while c!=i:
			ptr = ptr.next
			c=c+1
		v=ptr.val		
		ptr.next = pt.next.next
		return v
	def search(self,k):
		ptr=self.head
		while ptr!=None:
			if ptr.val == k:
				return ptr
			ptr=ptr.next
		return None

	def len(self):
		ptr=self.head
		c=0
		while ptr!=None:
			c=c+1
			ptr=ptr.next
		return c
	
	def printList(self):
		ptr=self.head
		ptr=ptr.next
		print("The list is :")
		while ptr!=None:
			print(ptr.val, end=',')
			ptr=ptr.next
		print('')

	def isEmpty(self):
		if self.len() == 0:
			return True
		else:
			return False
	
class Node:
	def __init__(self):
		self.val=0
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
        print("\nValue " + str(pt.val) + " is found at position " + str(c))
    else: 
        print("Value " + str(ch) + " not found")
   
if __name__ == '__main__':
    main()
