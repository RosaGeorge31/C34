def fib(n):
    a=0
    print(a, end = ' , ')
    b = 1
    print(b, end = ' , ')
    for i in range(2,n):
        c = a+b
        print(c, end=' , ')
        a = b
        b = c

def fibr(a,b,c,n):
    if c==0:
        print(c, end=' , ')
        fibr(a,b,1,n)
    elif c==1:
        print(c, end=' , ')
        fibr(a,b,2,n)
    elif c!=n:
        print(a+b, end=' , ')
        c = c+1
        fibr(b,a+b,c,n)
    else:
        return
        
        

num = int(input('Enter a number : '))
print('The factorial function result :')
fib(num)
print('')
print ('Using recursion : ')
fibr(0,1,0,num)
print('')
