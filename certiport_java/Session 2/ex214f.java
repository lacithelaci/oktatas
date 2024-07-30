class ex214f {

public static void main (String args[])
{
    int qty = 20;
    Integer reorder = new Integer("10");

    Boolean needsReorder = new Boolean("false");
    boolean mustReorder = needsReorder.booleanValue();

    if (qty < reorder) {
        mustReorder = true;
    }

    System.out.println(mustReorder);
    
    
}

}