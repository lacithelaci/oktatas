class ex313f {

public static void main (String args[])
{
    String customerStatus = "Gold";
    int bagQty = 8;
    double discount = 0;
    String discountMessage;

    if(customerStatus == "Gold")
    {
        if(bagQty >= 10) {
            discount = .10;
        }
        else{
            discount = .05;
        }
    }
    else if (customerStatus == "Silver")
    {
        if(bagQty >= 10) {
            discount = .05;
        }
        else{
            discount = .02;
        }
    }
    discountMessage = "Congratulations. Your " + customerStatus + " status gets you a " + discount * 100 + "% discount.";
    System.out.println(discountMessage);
}

}