public class Tea1 
{

// objective 4.2.1 

protected int teaID;
public String teaType;
public String teaName;
public double teaPrice;
private double salePrice = teaPrice * .7;

Tea1 (int teaID, String teaType, String teaName, double teaPrice) {
    this.teaID = teaID;
    this.teaType = teaType;
    this.teaName = teaName;
    this.teaPrice = teaPrice;
    this.salePrice = teaPrice * .7;
}
Tea1() {

}

public static void main (String args[])
{
   Tea1 t1 = new Tea1(1, "Herbal", "Mint Green", 9.99);
   System.out.println("Our first tea is " + t1.teaName + " sells for " + t1.teaPrice + " and is on sale now for " + String.format("%.2f",t1.salePrice));

   GourmetTea1 gt1 = new GourmetTea1(2, "Herbal", "Super Lotus", "Lotus");
   System.out.println("We have a new gourmet tea called " + gt1.teaName + " for " + gt1.teaPrice + ".");

}

}

class GourmetTea1 extends Tea1 
{
    public String gourmetBrand;

    GourmetTea1 (int teaID, String teaType, String teaName, String gourmetBrand)
    {
        this.teaID = teaID;
        this.teaType = teaType;
        this.teaName = teaName;
        this.gourmetBrand = gourmetBrand;
        this.teaPrice = 12.99;
        this.salePrice = 10.99;

    }
}
