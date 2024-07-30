

class ex131c {

public static void main (String args[])
{
    String location = "Arizona";
    double salesTax = 0;
    
        if (location == "Utah")
        {
            salesTax = .047;
            
        }
        else
        {
            otherStates();
        }

        System.out.println("Your sales tax rate is " + salesTax * 100 + "%.");
        
        
}

public static double otherStates() {
    salesTax = .05;
    return salesTax;
}

}