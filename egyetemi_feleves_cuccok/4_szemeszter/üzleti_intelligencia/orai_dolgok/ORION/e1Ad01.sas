/*Modify the path in quotes to match the 
location of the course data if necessary*/
libname orion "s:\workshop";

data children sports outdoors clothing;
set orion.products;
if Product_Line="Children" then
output children;
else if Product_Line="Sports" then
output sports;
else if Product_Line="Outdoors" then
output outdoors;
else output clothing;
run;

proc freq data=orion.products order=freq;
tables product_line / nocum;
title "Frequency Counts for Product Line";
run;
