import java.io.*;
class prg3
{
    public static void main(String args[])throws IOException
    {
        DataInputStream in = new DataInputStream(System.in);
       
        System.out.println("Enter the number of elements ");
        int n = Integer.parseInt(in.readLine());
        int a[] = new int[n];
        
        for(int i = 0;i<n;i++)
        {
            a[i] = Integer.parseInt(in.readLine());
        }
        System.out.println("Enter the number to be searched for: ");
        int val = Integer.parseInt(in.readLine());
        int flag = 0;
         for(int i = 0;i<a.length;i++)
        {
            if(a[i]==val)
            {
                flag = 1;
                System.out.println("Found at position : " + i);
             }           
        }
        if(flag==0)
        System.out.println("Element not found. ");
    }    
    
}
        
