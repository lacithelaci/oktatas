class ex241af {

public static void main (String args[])
{
   double bagSize = 12.9;
   int bagQty = 4;
   int bagSizeWhole = (int)(bagSize);
   String bagSizeString = String.valueOf(bagSize);

   System.out.println(bagSize);
   System.out.println(bagSizeWhole);
   System.out.println(bagSizeString);
   System.out.println(bagSize * bagQty);

}

}