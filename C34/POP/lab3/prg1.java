import java.io.*;
class prg1
{
    public static void main(String args[])throws IOException
        {
            DataInputStream in = new DataInputStream(System.in);
            int n1,n2,n3;
            System.out.println("Enter the first number");
            n1 = Integer.parseInt(in.readLine());
            System.out.println("Enter the second number");
            n2 = Integer.parseInt(in.readLine());
            System.out.println("Enter the third number");
            n3 = Integer.parseInt(in.readLine());
            if(n1<=n2 && n2<=n3)
            System.out.println("Increading order");
            else if (n1>=n2 && n2>=n3)
             System.out.println("Decreasing order");
            else
             System.out.println("Neither in Increading nor Descending order");
       }
}
            
