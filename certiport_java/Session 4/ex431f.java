public class ex431f {

    static String lastName = "Thomas";
    static String firstName = "Pat";


public static void main (String args[])
{
   String fullName = concatName();
   System.out.println(fullName);

   String lastNameFirstName = lastFirst();
   System.out.println(lastNameFirstName);

    String init = initials();
    System.out.println(init);

}

public static String concatName() {
    return firstName + " " + lastName;
}

protected static String lastFirst() {
    return lastName + ", " + firstName;
}

private static String initials() {
    return firstName.substring(0,1) + lastName.substring(0,1);
}


}

class GetNames {
    String fName = ex431.concatName();
    String lf = ex431.lastFirst();
    String i = ex431.initials();
}

