/*Using the concept of passing object as parameter implement a java program
to calculate total score of each students in class(consider 5 to 10 students and
5 subjects). */
import java.io.*;
class student
{
   String name;
   double m1;
   double m2;
   double m3;
   double m4;
   double m5;
   double total;
    public double calc(student o)
    {
        double ans = o.m1 + o.m2 + o.m3 + o.m4 + o.m5;
        return ans;
     }
        
    public static void main(String[] args)throws IOException
    {
        DataInputStream in = new DataInputStream(System.in);
        int n;
        String s="";
        System.out.println("Enter the number of students ");
        n = Integer.parseInt(in.readLine());
        student st[] = new student[n];
        for(int i = 0;i<n;i++)
        {
            st[i] = new student();
            System.out.println("Enter the student name followed by marks in 5 subjects");
            st[i].name = in.readLine();
            st[i].m1 = Double.parseDouble(in.readLine());
            st[i].m2 = Double.parseDouble(in.readLine());
            st[i].m3 = Double.parseDouble(in.readLine());
            st[i].m4 = Double.parseDouble(in.readLine());
            st[i].m5 = Double.parseDouble(in.readLine());
            st[i].total = st[i].calc(st[i]);
        }
        System.out.println("The details of all the students:");
        for(int i = 0;i<n;i++)
        {
            
            System.out.println("Name : " + st[i].name + "\tTotal marks: " + st[i].total);
        }
        
 }       
}

