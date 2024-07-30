class ex524f {

    static String [] cocoaBrands = new String[4];

public static void main (String args[])
{
    cocoaBrands[0] = "Regular";
    cocoaBrands[1] = "Dark Chocolate";
    cocoaBrands[2] = null;
    cocoaBrands[3] = "Sugar free";

    try
    {
        printItem(0);
        printItem(4);
        
    }
    catch(Exception e) {
        System.out.println(e.getClass());
        System.out.println(e.getMessage());
        System.out.println(e.fillInStackTrace());
    }
           
    finally
    {
        System.out.println("Code complete.");
    }
    
    
}
static void printItem(int item)
{
    
    System.out.println("Item number " + item + " is " + cocoaBrands[item]);
}

    
}

