str1 = input('Enter first string  ')
len1 = len(str1)
str2 = input('Enter second string  ')
len2 = len(str2)
str3 = input('Enter third string  ')
len3 = len(str3)
str4 =""
if len2>len1:
    print('Sorry wrong input')
else:
    i=0
    while i<len1:
             if str1[i:i+len2]==str2 :
                str4 = str4 + str3
              
                i = i+len2  
               
                if i>len1 :
                    break
                
             else:
                str4 = str4 + str1[i]
                i = i +1       
              
    print(str4)                
          
