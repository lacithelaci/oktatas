

class ex131cf {

    static double salesTax = 0;

public static void main (String args[])
{
    String location = "Arizona";
    
    
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