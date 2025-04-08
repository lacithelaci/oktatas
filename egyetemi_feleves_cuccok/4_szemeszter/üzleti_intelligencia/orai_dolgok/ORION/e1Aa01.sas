/*Modify the path in quotes to match the 
location of the course data if necessary*/

libname orion "s:\workshop";

data children(drop=Product_Category) sports outdoors clothing ;
	set orion.products;
	if Product_Line="Children" then output children;
	else if Product_Line="Sports" then output sports;
	else if Product_Line="Outdoors" then output outdoors;
	else output clothing;
	drop Product_Line;
run;

proc print data=childrens noobs label;
	title "Product Line: Children";
run;