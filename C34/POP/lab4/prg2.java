import java.io.*;
class prg2
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
        prg2 obj = new prg2();
        System.out.println("The result : " + obj.sum30(a));
    }
    
    boolean sum30(int[] A)
    {
        int ct=0;
         for(int i = 0;i<A.length;i++)
        {
            if(A[i]==10)
            ct++;
         }
        if(ct==3)
        return true;
        else
        return false;
    }    
    
}
        
