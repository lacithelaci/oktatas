class ex432f {

static String location = "UT";

public static void main (String args[])
{
   double order1 = orderTotal(5, 9.99);
   double order2 = orderTotal(4, 8.99);

   System.out.println("Your first order total is " + String.format("%.2f", order1));
   System.out.println("Your second order total is " + String.format("%.2f", order2));


}

public static double orderTotal(int qty, double price)
{
    double amount;
    if(location == "UT")
    {
        amount = qty * price * 1.06;
    }
    else
    {
        amount = qty * price;
    }
    return amount;
}

}