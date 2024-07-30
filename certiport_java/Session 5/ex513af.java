class ex513af {

public static void main (String args[])
{
   int orderQty = 50;
   String customerStatus = "";

   if (orderQty >= 80)
   {
       customerStatus = "Gold";
   }
   else if (orderQty >= 40)
   {
       customerStatus = "Silver";
   }

   System.out.println("Your customer status is " + customerStatus);
}

}