import java.util.*;
class matrixaddd
{
   int[][] a=new int[3][3];
   int[][] b=new int[3][3];
   int[][] c=new int[3][3];
   
   
   void read()
   {
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the elements in first matrix:");
    for(int i=0;i<3;i++)
    {
     for(int j=0;j<3;j++)
     {
      a[i][j]=sc.nextInt();
     }
    }
    System.out.println("Enter the elements in second matrix:");
    for(int i=0;i<3;i++)
    {
     for(int j=0;j<3;j++)
     {
      b[i][j]=sc.nextInt();
     }
    }
   } 
   
    void display()
    {
    
    for(int i=0;i<3;i++)
    {
     for(int j=0;j<3;j++)
     {
      c[i][j]=a[i][j]+b[i][j];
 
     }
    }
    System.out.println("Sum of Matrix: ");
    for(int i=0;i<3;i++)
    {
     for(int j=0;j<3;j++)
     {
      System.out.print(c[i][j]+" ");
     }
     System.out.println("");
    }
   }
   public static void main(String args[])
   {
    matrixaddd k=new matrixaddd();
    k.read();
    k.display();
   }  
}
