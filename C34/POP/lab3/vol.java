import java.io.*;
class vol
{
  int d1,d2,d3;
  
  vol(int r)
  {
  d1 = r;
  }
  
  vol(int l, int b)
  {
  d1 = l;
  d2 = b;
  }
  
  vol(int l, int b, int h)
  {
  d1=l;
  d2 = b;
  d3 = h;
  }
  
  void volume(int s)
  {
    double vol = Math.pow(s,3);
    System.out.println("Volume of cube : " + vol);
  }
  
  void volume(int l, int b, int h)
  {
    double vol = l*b*h ;
    System.out.println("Volume of cuboid : " + vol);
  }
  
  double volume(int h,int r)
  {
     double vol = 3.14 * h * Math.pow(r,2);
     System.out.println("Volume of cylinder : " + vol);
  }
 
 
  
  public static void main(String args[])throws IOException
  {
        DataInputStream in = new DataInputStream(System.in);
        int ch,s,l,b,h,r,h2;
        double ans =0.0;
        do
        {
           System.out.println("1. Volume of a cube");  
            System.out.println("2. Volume of a cuboid");
            System.out.println("3. Volume of a cylinder");
            System.out.println("4. Volume of a cone");
            System.out.println("5. Exit");          
            ch = Integer.parseInt(in.readLine());
            
            switch(ch)
            {
             case 1: 
                    System.out.println("Enter the side");
                    s= Integer.parseInt(in.readLine());
                    vol obj = new vol(s);
                    obj.volume(s);
                    break;
           case 2: 
                    System.out.println("Enter the length, breadth and height");
                    l = Integer.parseInt(in.readLine());
                    b = Integer.parseInt(in.readLine());
                    h = Integer.parseInt(in.readLine());
                    vol obj2 = new vol(l,b,h);
                    obj2.volume(l,b,h);
                    break;
          case 3: 
                    System.out.println("Enter the radius and height");
                    r = Integer.parseInt(in.readLine());
                    h2 = Integer.parseInt(in.readLine());
                    vol obj3 = new vol(r,h2);
                    obj3.volume(h2,r);
                    break;
                    case 4: 
                    System.out.println("Enter the radius and height");
                    r = Integer.parseInt(in.readLine());
                    h2 = Integer.parseInt(in.readLine());
                    vol obj4 = new vol(r,h2);
                    ans = obj4.volume(h2,r);
                    System.out.println("The volume = " + ans/3);
                    break;
            }
            }while(ch!=5);
            }
            }
  
  
  
