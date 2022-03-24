import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main
{
	public static void main(String[] args)throws Exception
	{
		findSalary("12");
	}

	static void findSalary(String empId)throws IOException
	{
		// finding the employee Name
		int employeeIdColumnNumber = 0;
		int employeeNameColumnNumber = 0;
		File empDetailsFile = new File("employeeDetailsFileName.csv");
		Scanner employeeFileScanner = new Scanner(empDetailsFile);
		String[] columnNames = employeeFileScanner.nextLine().split(",");
		for (int i=0;i<columnNames.length;i++)
		{
			switch (columnNames[i].trim())
			{
				case "emp_id":
					employeeIdColumnNumber = i;
					break;
				case "emp_name":
					employeeNameColumnNumber = i;
					break;
			}
		}
		String employeeName = null;
		while (employeeFileScanner.hasNextLine())
		{
			String[] rowValues = employeeFileScanner.nextLine().split(",");
			try
			{
				if (rowValues[employeeIdColumnNumber].equals(empId))
				{
					employeeName = rowValues[employeeNameColumnNumber].trim();
					break;
				}
			}
			catch (ArrayIndexOutOfBoundsException ignored)
			{}
		}

		// finding the employee Salary
		employeeIdColumnNumber = 0;
		int salaryColumnNumber = 0;
		int pfColumnNumber = 0;
		File empSalaryFile = new File("employeeSalaryFileName.csv");
		Scanner salaryFileScanner = new Scanner(empSalaryFile);
		columnNames = salaryFileScanner.nextLine().split(",");
		for (int i=0;i<columnNames.length;i++)
		{
			switch (columnNames[i].trim())
			{
				case "emp_id":
					employeeIdColumnNumber = i;
					break;
				case "salary":
					salaryColumnNumber = i;
					break;
				case "pf":
					pfColumnNumber = i;
					break;
			}
		}
		String salary = null;
		String pf = null;
		while (salaryFileScanner.hasNextLine())
		{
			String[] rowValues = salaryFileScanner.nextLine().split(",");
			try
			{
				if (rowValues[employeeIdColumnNumber].equals(empId))
				{
					salary = rowValues[salaryColumnNumber].trim();
					pf = rowValues[pfColumnNumber].trim();
					break;
				}
			}
			catch (ArrayIndexOutOfBoundsException ignored)
			{}
		}

		//printing
		System.out.println("Employee Name: " + employeeName);
		System.out.println("Salary: " + salary);
		System.out.println("Pf: " + pf);
	}
}
