class emp
{
    String name;
    float salarypm;
    float bonus;
    
    emp(String n,float s, float b)
    {
        name = n;
        salarypm = s;
        bonus = b;
    }
     
     float totalsalary(int t)
     {
        return salarypm*t + bonus;
     }
     void display(String n, float sal)
     {
        System.out.println("Name : " + n + "\t Salary: " + sal);
        
     }
        
     public static void main(String args[])
     {
        emp person1 = new emp("Tom",1000,50);
        float ans = person1.totalsalary(5);
        person1.display(person1.name,ans);
        
         emp person2 = new emp("Jill",8000,150);
        ans = person2.totalsalary(9);
        person2.display(person2.name,ans);
        }
}
