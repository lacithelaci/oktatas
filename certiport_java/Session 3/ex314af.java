class ex314af {

public static void main (String args[])
{
    String frRoast = "in";
    String medRoast = "in";
    String italRoast = "out";
    String italRoastDecaf = "out";
    String houseDecaft = "in";

    boolean bothDarks, oneDark;

    bothDarks = frRoast == "in" && italRoast == "in";
    oneDark = frRoast == "in" || italRoast == "in";

    System.out.println(bothDarks + "\t" + oneDark);
}

}