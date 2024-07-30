public class Tea2 
{

// objectives 4.2.2 and 4.2.3 

protected int teaID;
public String teaType;
public String teaName;
public double teaPrice;
private double salePrice = teaPrice * .7;

Tea2 (int teaID, String teaType, String teaName, double teaPrice) {
    this.teaID = teaID;
    this.teaType = teaType;
    this.teaName = teaName;
    this.teaPrice = teaPrice;
    this.salePrice = teaPrice * .7;
}
Tea2() {

}

public static void main (String args[])
{
   Tea2 t2 = new Tea2(1, "Herbal", "Mint Green", 9.99);
   System.out.println("Our first tea is " + t2.teaName + " sells for " + t2.teaPrice + " and is on sale now for " + String.format("%.2f",t2.salePrice));

   GourmetTea2 gt2 = new GourmetTea2(2, "Herbal", "Super Lotus", "Lotus");
   System.out.println("We have a new gourmet tea called " + gt2.teaName + " on sale for " + gt2.gourmetSalePrice + ".");

}

}

class GourmetTea2 extends Tea2 
{
    public String gourmetBrand;
    static double gourmetSalePrice = 10.99;

    GourmetTea2 (int teaID, String teaType, String teaName, String gourmetBrand)
    {
        this.teaID = teaID;
        this.teaType = teaType;
        this.teaName = teaName;
        this.gourmetBrand = gourmetBrand;
        this.teaPrice = 12.99;
        

    }
}
