import java.io.*;
class prg6
{
    
   
    int findLengthlong(int arr[], int n) 
    {
        int max_len = 1;  // Initialize result
        for (int i = 0; i < n - 1; i++) 
        {
          
            int mn = arr[i], mx = arr[i];
            for (int j = i + 1; j < n; j++) 
            {
               
                mn = (mn<arr[j]) ? mn : arr[j];
                mx = (mn>arr[j]) ? mn : arr[j];
 
                if ((mx - mn) == j - i)
                    max_len =  max_len>(mx-mn+1)?max_len:(mx - mn + 1);
                   
            }
        }
        return max_len;  // Return result
    }
 
        int findLengthmin(int arr[], int n) 
        {
        int min_len = 1;  // Initialize result
             for (int i = 0; i < n - 1; i++) 
             {
          
                    int mn = arr[i], mx = arr[i];
                   for (int j = i + 1; j < n; j++) 
                     {
               
                mn = (mn<arr[j]) ? mn : arr[j];
                mx = (mn>arr[j]) ? mn : arr[j];
 
                if ((mx - mn) == j - i)
                    min_len =  min_len<(mx-mn+1)?min_len:(mx - mn + 1);
                   
            }
        }
        return min_len;  // Return result
    }
    public static void main(String[] args) throws IOException
    {
        DataInputStream in = new DataInputStream(System.in);
        prg6 large = new prg6();
        System.out.println("Enter the number of elements : ");
        int n = Integer.parseInt(in.readLine());
        int[] arr = new int[n];
        for(int i = 0;i<n;i++)
            arr[i] = Integer.parseInt(in.readLine());
        for(int i = 0;i<n;i++)
            {
                for(int j = 0; j<n-1; j++)
                    { 
                            if(arr[j]>arr[j+1])
                            {
                                int t = arr[j];
                                arr[j] = arr[j+1];
                                arr[j+1] = t;
                            }
                    }
           }
        System.out.println("Length of the longest contiguous subarray is "
                + large.findLengthlong(arr, n));
          System.out.println("Length of the smallest contiguous subarray is "
                + large.findLengthmin(arr, n));        
    }
}
 
