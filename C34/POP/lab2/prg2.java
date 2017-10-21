import java.io.*;
class prg2
{
	public static void main(String args[])throws IOException
	{
		DataInputStream in = new DataInputStream(System.in);
		int n,tmp;
		String s= "";
		System.out.println("Enter the number:");
		n = Integer.parseInt(in.readLine());
		tmp = n;
		
		while(tmp!=1)
		{
			if(tmp%2!=0)
			s = "1" +s;
			else
			s = "0" + s;
			tmp/=2;
		}
			s = "1" +s;
		System.out.println("The binary equivalent of " + n + " is " + s);

	}
}

		
