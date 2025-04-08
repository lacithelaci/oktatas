/*Change the path within quotes (if necessary) to
point to the location of the course data files.*/
libname orion "s:\workshop";
data CurrentEmployees;
merge orion.employee_payroll(where=(Employee_Term_Date is missing) in=InPayroll) 
orion.employee_organization;by Employee_ID;if InPayroll=1;format Birth_Date Employee_Hire_Date mmddyy10. salary dollar12.;run;
proc gchart data=CurrentEmployees;hbar Department/sumvar=Salary type=mean patternid=midpoint;
title "Average Salary by Department";run;