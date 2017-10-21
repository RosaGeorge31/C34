def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return 'False'
    return 'True'
 
num = int(input('Enter a number : '))
print("\nIs the number a prime number?\n" + isPrime(num))
        

