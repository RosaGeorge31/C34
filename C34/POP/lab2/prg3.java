import java.io.*;
class prg3
{
	public static void main(String args[])throws IOException
	{
		DataInputStream in = new DataInputStream(System.in);
		int n,tmp=0,i,t2=0;
		int f = 0;
		String s= "",s2 = "";
		System.out.println("Enter the equation:");
		s = (in.readLine());
		for(i=0;i<s.length();i++)
		{
			if(s.charAt(i)=='x'&& i!=0)
			{
				tmp = i-1;
			}
			else if(s.charAt(i)=='x'&& i==0)
			{
				f = 1;
				tmp = i;
			}
			else if(s.charAt(i)=='=')
				t2 = i;
			else
				continue;
		}
		
		int temp = 0,fl=0;
		int ans =0,count=0;
		s2 = s.substring(t2+1,s.length());
		char vals[] = new char[s2.length()];
		int ct =0;
		for(i = 0;i<s2.length();i++)
		{
			vals[i] = s2.charAt(i);
		}

		for(i = 0;i<s2.length();i++)
		{
			temp = 0;
			++count;
			while(Character.isDigit(vals[i])==true)
					{
						temp = temp*10 + (vals[i]-48);			
						++i;
						if(i==s2.length())
						break;
					}

			if(count==1)
			{
				ans+=temp;
				continue;
			}
			if((i+1)!=s2.length())
			{
			switch(vals[i])
			{
				case '+' :temp = 0;fl=0;
					 while(Character.isDigit(vals[i+1])==true)
					{
						temp = temp*10 + (vals[i+1]-48);			
						++i;
						if(i==s2.length())
						{
							fl=1;
						break;
						}
					}
					ans+=temp;
			}
			}
			if(fl==1)
			break;
		}
			System.out.println("Ans : " + ans);

		/*for(i = 0;i<s2.length();i++)
		{
			if(Character.isDigit(s2.charAt(i))==true)
			{
				int j = i;
				temp = 0;
				while(Character.isDigit(s2.charAt(j))==true)
					{
						temp = temp*10 + (s2.charAt(j)-48);
						++ct;
						j++;
						if(j==s2.length())
						break;
					}
				i = j;
				System.out.println("Value : " + temp);
			}
		}							
		*/

	}
}

		
