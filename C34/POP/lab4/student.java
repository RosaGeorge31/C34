import java.io.*;
class student
{
    String name;
    int rollno;
    float marks;
    int sem;
    
    student(String n,int no,float m, int s)
    {
        name = n;
        rollno = no;
        sem = s;
        marks = m;
    }
     
     
     void display()
     {
        
        System.out.println("Name : " + this.name + "\t Roll Number: " + this.rollno + "\t Semester: " + this.sem + "\t Marks: " + this.marks);
        
     }
        
     public static void main(String args[])throws IOException
     {
        DataInputStream in = new DataInputStream(System.in);
        System.out.println("Enter the number of elements");
        int n = Integer.parseInt(in.readLine());
        String s;
        int sem,roll;
        float marks;
        student[] obj = new student[n];
        for(int i = 0;i<n;i++)
        {
            System.out.println("Enter the name, roll number, marks and semester of student :" + i+1);
            s = in.readLine();
            roll = Integer.parseInt(in.readLine());
            marks = Float.parseFloat(in.readLine());
            sem = Integer.parseInt(in.readLine());
            obj[i] = new student(s,roll,marks,sem);
        }
             System.out.println("\nThe student details :" );
        for(int i = 0;i<n;i++)
        {
            obj[i].display();
        }
        }
}
