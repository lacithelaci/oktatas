import java.io.*;

class ex523b {

public static void main (String args[])
{
   FileInputStream testFile = null;

   try
   {
       testFile = new FileInputStream("test.txt");
       System.out.println("Test file found");

   }
   catch(FileNotFoundException ex) {
       System.out.println("Test file not found");
   }

}

}