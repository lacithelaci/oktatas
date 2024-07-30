class ex314af {

public static void main (String args[])
{
    String frRoast = "in";
    String medRoast = "in";
    String italRoast = "out";
    

    if (frRoast == "in" && italRoast == "in") {
        System.out.println("Both darks are in stock.");
    }
    else if (frRoast == "in" || italRoast == "in") {
        System.out.println("One dark is in stock.");
    }
    
}

}