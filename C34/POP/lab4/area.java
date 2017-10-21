import java.io.*;
class area
{
  int d1,d2,d3;
  
  area(int r)
  {
  d1 = r;
  }
  
  area(int l, int b)
  {
  d1 = l;
  d2 = b;
  }
  
  area(int l, int b, int h)
  {
  d1=l;
  d2 = b;
  d3 = h;
  }
  
  void areaf(int s)
  {
    double area = Math.pow(s,2) *22 /7 *3;
    System.out.println("\nArea of hemisphere : " + area);
  }
  
  void areaf(int l, int b, int h)
  {
    double area = 2*(l*b + l*h + b*h) ;
    System.out.println("\nArea of rectangular prism : " + area);
  }
  
  void areaf(int h,int r)
  {
     double area = 22 / 7 * r * (r + Math.sqrt(Math.pow(r,2) + Math.pow(h,2)));
     System.out.println("\nArea of cone : " + area);
      
  }
 
  void areafig(int l,int w, int h)
  {
    double area = l*w + (l* Math.sqrt(Math.pow(w/2,2)+Math.pow(h,2))) + (w* Math.sqrt(Math.pow(l/2,2)+Math.pow(h,2))) ;
    System.out.println("\nArea of rectangular pyramid : " + area);
    
   }
    
  double areafig(int h,int r)// cylinder
    {  
        double area = 44 / 7 * r * (r +h);
        return area;
     }
  
  public static void main(String args[])throws IOException
  {
        DataInputStream in = new DataInputStream(System.in);
        int ch,s,l,b,h,r,h2;
        double ans =0.0;
        do
        {
           System.out.println("1. Area of a hemisphere");  
            System.out.println("2. Area of a prism");
            System.out.println("3. Area of a cylinder");
            System.out.println("4. Area of a cone");
            System.out.println("5. Area of a pyramid");
            System.out.println("6. Exit");          
            ch = Integer.parseInt(in.readLine());
            
            switch(ch)
            {
             case 1: 
                    System.out.println("Enter the radius");
                    s= Integer.parseInt(in.readLine());
                    area obj = new area(s);
                    obj.areaf(s);
                    break;
           case 2: 
                    System.out.println("Enter the length, breadth and height");
                    l = Integer.parseInt(in.readLine());
                    b = Integer.parseInt(in.readLine());
                    h = Integer.parseInt(in.readLine());
                     area obj2 = new area(l,b,h);
                    obj2.areaf(l,b,h);
                    break;
          case 3: 
                    System.out.println("Enter the radius and height");
                    r = Integer.parseInt(in.readLine());
                    h2 = Integer.parseInt(in.readLine());
                    area obj3 = new area(r,h2);
                    System.out.println("\nArea of cylinder : " + obj3.areafig(h2,r));
                    break;
          case 4: 
                    System.out.println("Enter the radius and height");
                    r = Integer.parseInt(in.readLine());
                    h2 = Integer.parseInt(in.readLine());
                    area obj4 = new area(r,h2);
                    obj4.areaf(h2,r);
                    break;
          case 5:  System.out.println("Enter the length, breadth and height");
                    l = Integer.parseInt(in.readLine());
                    b = Integer.parseInt(in.readLine());
                    h = Integer.parseInt(in.readLine());
                     area obj5 = new area(l,b,h);
                    obj5.areafig(l,b,h);
                    break;
            }
         }while(ch!=6);
   }
}
  
  
  
