
n = int(input('Enter the number of elements : '))
a = [0]*n
b=  [0]*n
for i in range(0,n):
    a[i] = int(input('Enter an element : '))
    b[i] = a[i]
for i in range(0,n):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            
    
print('Bubble Sorted:')
for i in range(0,n):
    print(a[i])
   
for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
        if b[j]<b[min]:
            temp = b[j]
            b[j] = b[min]
            b[min] = temp
            
    
print('Selection Sorted:')
for i in range(0,n):
    print(b[i])   
