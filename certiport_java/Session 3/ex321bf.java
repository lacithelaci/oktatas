class ex321bf {

public static void main (String args[])
{
   int totalOrders = 1;
   int orderCount = 1;

   

    do
   {
        System.out.println("An order will be sent to you in " + orderCount * 30 + " days.");
        orderCount++;
   }
   while(orderCount < totalOrders);
}

}