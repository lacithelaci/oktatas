class ex515 {

    static String [] cocoaBrands = new String[4];

public static void main (String args[])
{
    cocoaBrands[0] = "Regular";
    cocoaBrands[1] = "Dark Chocolate";
    cocoaBrands[2] = null;
    cocoaBrands[3] = "Sugar free";

    printItem(0);
    printItem(4);
    
    

}
static void printItem(int item)
{
    
    System.out.println("Item number " + item + " is " + cocoaBrands[item]);
}

    

}

