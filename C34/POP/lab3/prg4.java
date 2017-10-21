import java.io.*;
class prg4
{
    public static void main(String args[])throws IOException
        {
            DataInputStream in = new DataInputStream(System.in);
            int n1,n2,i,j;
            System.out.println("Enter the number of elements of array 1");
            n1 = Integer.parseInt(in.readLine());
           int a[] = new int[n1];
            System.out.println("Enter the elements");
            for(i = 0;i<n1; i++)
            {
                a[i] = Integer.parseInt(in.readLine());
            }
           System.out.println("Enter the number of elements of array 2");
            n2 = Integer.parseInt(in.readLine());
           int b[] = new int[n2];
            System.out.println("Enter the elements");
            for(i = 0;i<n2; i++)
            {
                b[i] = Integer.parseInt(in.readLine());
            }
            int ct =0;
            for(i = 0;i<n1;i++)
            {
                for(j = 0; j<n2; j++)
                    { 
                            if(a[i]==a[j])
                            {
                                ct++;
                                break;
                            }
                    }
           }
            System.out.println("ct = " + ct);           
       }
}
            
