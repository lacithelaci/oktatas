class ex513 {

public static void main (String args[])
{
   int orderQty = 105;
   String customerStatus = "";

   if (orderQty >= 40)
   {
       customerStatus = "Silver";
   }
   else if (orderQty >= 80)
   {
       customerStatus = "Gold";
   }

   System.out.println("Your customer status is " + customerStatus);
}

}