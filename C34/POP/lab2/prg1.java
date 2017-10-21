import java.io.*;
class prg1
{
	public static void main(String args[])throws IOException
	{
		DataInputStream in = new DataInputStream(System.in);
		int a,b,c,ch;
		double d;
		System.out.println("Enter the first number:");
		a = Integer.parseInt(in.readLine());
		System.out.println("Enter the second number:");
		b = Integer.parseInt(in.readLine());
		do
		{
			System.out.println("\n1. Addition");
			System.out.println("2. Subtraction");
			System.out.println("3. Multiplication");
			System.out.println("4. Division");
			System.out.println("5. Quit");
			System.out.println("Enter your choice");
			ch = Integer.parseInt(in.readLine());
			switch(ch)
			{
				case 1: c= a+b;
						System.out.println("The sum = " + c);
				break;
				case 2: c= a-b;
						System.out.println("The difference = " + c);
				break;
				case 3: c= a*b;
						System.out.println("The product = " + c);
				break;
				case 4: d= (double)a/(double)b;
						System.out.println("The quotient = " + d);
				break;
			}
		}while(ch!=5);
	}
}

		
