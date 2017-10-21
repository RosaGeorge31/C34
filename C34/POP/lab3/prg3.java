import java.io.*;
class prg3
{
    public static void main(String args[])throws IOException
        {
            DataInputStream in = new DataInputStream(System.in);
            int n,i,j;
            System.out.println("Enter the number of elements");
            n = Integer.parseInt(in.readLine());
           int a[] = new int[n];
            System.out.println("Enter the elements");
            for(i = 0;i<n; i++)
            {
                a[i] = Integer.parseInt(in.readLine());
            }
           
            for(i = 0;i<n;i++)
            {
                for(j = 0; j<n-1; j++)
                    { 
                            if(a[j]>a[j+1])
                            {
                                int t = a[j];
                                a[j] = a[j+1];
                                a[j+1] = t;
                            }
                    }
           }
              System.out.println("the elements");
            for(i = 0;i<n; i++)
            {
               System.out.println(a[i]);
            }
			System.out.println("the elements");
            
           int max = 0,f=0;
           int min = 100000000;
           int ct = 0;
			/*
			int count = 1;

			for (i = 1; i < n; i++) {
    			if (a[i] >= a[i - 1]) {
   				     count++;
   				 } else {
       			 count = 1;
    			}

    if (count > max) {
        max = count;
    }
}*/
           for(i = 0;i<n-1;i++)
           {    ct = 0;
				System.out.println("DIFF " + (a[i+1]-a[i]));
                while(a[i+1]-a[i] == 1)
                {
					System.out.println(i+" in ");
            		ct++;
                    i++;
                    if(i>n)
                    {
                    f=1;
                    break;
                    }
                }
                
                if(f==1)
                break;
                
                if(ct>max)
                {
				i--; max = ct;
				}
                if(ct<min)
                {
				i--; min = ct;
				}
            }
            
            System.out.println("max = " + max);           
       }
}
            
