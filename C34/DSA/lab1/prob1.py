def fact(n):
    f = 1
    for i in range(2,n+1):
            f = f * i
    print(f)
def factr(n):
    if n==0 or n==1:
        return 1
    else:
        return (n * factr(n-1))
        
num = int(input('Enter a number :'))
print("Using the factorial function :")
fact(num)
ans = factr(num)
print("With recursive function : " + str(ans))

