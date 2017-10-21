import java.io.*;
class prg1
{
    public static void main(String args[])throws IOException
    {
        DataInputStream in = new DataInputStream(System.in);
        int val;
        String s[] = {"","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"};
        System.out.println("Enter a number ");
        
        val = Integer.parseInt(in.readLine());
        if(val>7)
        {
            while(val>7)
            {
                val = val%7;
            }
        }
        System.out.println("The day : " + s[val]);
    }
}
        
