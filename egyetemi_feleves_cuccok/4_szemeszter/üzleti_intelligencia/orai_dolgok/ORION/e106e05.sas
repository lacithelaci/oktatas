data address_labels;
	/*Modify the path in quotes if necessary to point to
		the location of the course data*/
	set "s:\workshop\employee_master.sas7bdat";
	Line1 = catx(" ",scan(Employee_Name,2,","),scan(Employee_Name,1,","));
	Line2 = catx(" ",Street_Number, Street_Name);
	if State = " " then 
		Line3 = catx(", ",City, "Australia");
	else Line3 = catx(", ",City,State);
	keep Department Line1 Line2 Line3;
	/*Modify the following statement to reference a prompt*/
	where Department = "Administration";
run;
