import java.util.*;
class employee
{
 int emp_no,emp_salary;
 String emp_name;
 void read()
 {
  Scanner sc= new Scanner(System.in);
  System.out.println("Enter the Employee No:");
  emp_no=sc.nextInt();
  System.out.println("Enter the Employee name:");
  emp_name=sc.next();
  System.out.println("Enter the Employee Salary:");
  emp_salary=sc.nextInt();
 }
 void search(int temp_no)
 {
 if(emp_no==temp_no)
 {
  System.out.println("Searched "+temp_no+" Found");  
  System.out.println("Employee NO: "+emp_no);
  System.out.println("Employee name: "+emp_name);
  System.out.println("Employee salary "+emp_salary);
 }
 }
 public static void main(String args[])
 {
 Scanner sc= new Scanner(System.in);
  employee emp[] = new employee[3];
  for(int i=0;i<3;i++)
  {
   emp[i]=new employee();
   emp[i].read();
  }
  System.out.println("Enter the emp_no to be searched");
  int temp_no = sc.nextInt();
  for(int i=0;i<3;i++)
  {
   emp[i].search(temp_no);
  }
 }
}
