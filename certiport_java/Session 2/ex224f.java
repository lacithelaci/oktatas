class ex224f {

public static void main (String args[])
{
    String name = "Tracy";
    int qty = 5;
    String product = "Mint Cocoa";

    System.out.println (name + ", thank you for your order of " + Integer.toString(qty) + " cans of " + product + ".");
    System.out.println (name + ", thank you for your order of " + String.valueOf(qty) + " cans of " + product + ".");
}

}