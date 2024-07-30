class ex441f {

public static void main (String args[])
{
   
    Product prod1 = new Product(1, "Tea", "Green Tea", 8.99);
    System.out.println("Our first tea is " + prod1.productName + ".");
    Product prod2 = new Product(2, "Coffee", "Colombian", 7.99);
    System.out.println("Our first coffee is " + prod2.productName + ".");
  
}
static class Product 
{
    int productId;
    String type;
    String productName;
    double price;

   Product(int productIdValue, String typeValue, String productNameValue, double priceValue)
   {
        productId = productIdValue;
        type = typeValue;
        productName = productNameValue;
        price = priceValue;

   }
}

}

