public class Tea1 {

// objective 4.2.1 

protected int teaID;
public String teaType;
public String teaName;
public double teaPrice;
private double salePrice = teaPrice * .7;

void Tea1 (int teaID, string teaType, string teaName, string teaPrice) {
    this.teaID = teaID;
    this.teaType = teaType;
    this.teaName = teaName;
    this.teaPrice = teaPrice;
    this.salePrice = teaPrice * .7;
}

public static void main (String args[])
{
   Tea1 t1 = new Tea1(1, "Herbal", "Mint Green", 9.99);
   System.out.println("Our first tea is " + t1.teaName, " sells for " + t1.teaPrice + " and is on sale now for " + t1.salePrice);
}

}