def main():

    s = input("Enter the string: ")
    a = s.split()
    op = ['+','-','*','/']
    for i in range(len(a)):    
        if a[i]=='(':                        
            T.insertLeft(curr,a[i])
        

if __name__=='__main__':
    main()
    
