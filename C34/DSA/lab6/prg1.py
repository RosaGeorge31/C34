import math
class BinaryHeap:
    def __init__(self):
        self.L = []
        
        self.top = -1
       
    def insert(self,val):
        if self.top == -1:
            self.top = 0
            self.L.append(val)
            return
        self.top+=1
        self.L.append(val)
        self.heapify(self.L,self.top)
        
    def maximum(self):
        if self.top == -1:
            print("Underflow!")
            return None
        
        v = self.L[0]
        return v

    def extractmax(self):
        if self.top == 0:
            print("Underflow!")
            return None
        
        v = self.L[0]
        self.L[0] = self.L[self.top]
        self.L[self.top] = None
        self.top = self.top -1 
        self.heapify(self.L,self.top)

    def getleft(self,pos):
        return self.L[2*pos +1 ]

    def getposright(self,pos):
        return 2*pos+2

    def getright(self,pos):
        return self.L[2* pos +2]
    
    def parent(self,pos):
        return self.L[math.floor(pos/2)]

    def heapify(self,arr,pos):
        
        if pos%2==0 and pos!= 0:
            po = (pos-1)
        else:
            po = pos
        par = self.parent(po)
       
        while pos!=0 and par<=arr[pos]:
            
            rpos = self.getposright(math.floor(po/2))    
            
            if rpos > self.top:
                val1 = 0
                val2 = arr[pos]
            else:
                val1 = arr[rpos]
                val2 = arr[rpos-1]
            
            if val1>val2:
                temp = par
                self.L[math.floor(po/2)] = val1
                self.L[pos] = temp
                
            else:
                temp = par
                self.L[math.floor(po/2)] = val2
                self.L[pos] = temp
            pos=math.floor(po/2)
            if pos%2==0:
                po = (pos-1)
            else:
                po = pos
            par = self.parent(po)

    def build_heap(self,arr,le):
        Len = le
        while Len!=0:
            self.heapify(self.L,Len)
            Len= Len -1
        

    def display(self):
        print("displaying:")
        for i in self.L:
            print(i)

def main():
    
    H = BinaryHeap()
    H.insert(20)
    H.insert(2)
    H.insert(10)
    H.insert(3)
    H.insert(5)
    H.insert(12)
    H.insert(30)
    H.insert(23)
    H.insert(230)
    H.insert(40)
    H.display()
    H2 = BinaryHeap()
    a = [20, 2, 10,3 , 5, 12, 30, 23, 230,40]
    H2.L = a
    H2.build_heap(a,9)
    H2.display()

if __name__=='__main__':
    main()                
        
                













        
        
