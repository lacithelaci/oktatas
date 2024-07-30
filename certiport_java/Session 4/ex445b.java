import java.util.Date;

class ex445b {

public static void main (String args[])
{
   Tea1 t6 = new Tea1(6, "Regular" , "Raspberry", 6.99);
   Date currentDate = new Date();
  
   System.out.println("Our new tea is " + t6.teaName + ", on sale as of " + currentDate);
}

}