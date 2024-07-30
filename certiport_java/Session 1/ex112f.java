class ex112f {

public static void main (String args[])
{
    Product product1 = new Product("Coffee", "Medium Roast", 9.99);
    Product product2 = new Product("Tea", "Organic White", 7.99);

    System.out.println(product1.name);
    System.out.println(product2.name);
}

}

class Product {

    String type;
    String name;
    double price;

    Product(String type, String name, double price) {
        this.type = type;
        this.name = name;
        this.price = price;
    }
}