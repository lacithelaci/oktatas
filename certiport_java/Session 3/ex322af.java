class ex322af {

public static void main (String args[])
{
    String [] cocoaBrands = new String[4];

    cocoaBrands[0] = "Regular";
    cocoaBrands[1] = "Dark Chocolate";
    cocoaBrands[2] = null;
    cocoaBrands[3] = "Sugar free";

   for (int c=0; c<cocoaBrands.length; c++) {
       if (cocoaBrands[c] == null) {
           break;
       }
        System.out.println(cocoaBrands[c]);
    }

}

}