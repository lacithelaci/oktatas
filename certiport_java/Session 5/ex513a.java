class ex513a {

public static void main (String args[])
{
   int orderQty = 45;
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