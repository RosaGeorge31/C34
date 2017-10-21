import java.io.*;
class prg2
{
    public static void main(String args[])throws IOException
        {
            DataInputStream in = new DataInputStream(System.in);
            double ans ,amt,t,r;
            System.out.println("Enter the investment amount");
            amt = Double.parseDouble(in.readLine());
            System.out.println("Enter the rate of interest");
            r = Double.parseDouble(in.readLine());
            System.out.println("Enter the number of years");
            t = Double.parseDouble(in.readLine());
            System.out.println("Years \tFuture Value");
            for(int i = 1;i <=(int)t; i++)
            {
                double tmp = r/1200;
                ans = amt * Math.pow(1+tmp, 12 *i);
                System.out.println(i + " \t" + ans);
            }           
       }
}
            
