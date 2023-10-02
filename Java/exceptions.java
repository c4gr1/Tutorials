import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.io.FileWriter;


public class exceptions {
    public static void main(String[] args) {
        //yaz();
        oku();
    }

    public static void yaz(){

        File file = new File("read.txt");
        FileWriter fileWriter = null;
        Scanner scanner = new Scanner(System.in);

        try {
            fileWriter = new FileWriter(file);
            System.out.print("Bir yazı giriniz: ");
            fileWriter.write(scanner.nextLine());
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        finally{
            try {
                fileWriter.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            scanner.close();
        }
    }
    
    public static void oku(){

        File file = new File("read.txt");

        FileReader fileReader = null;

        try {
            fileReader = new FileReader(file);
            int c =0;

            while((c = fileReader.read()) != -1){
                System.out.print((char) c);
            }

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        finally{
            if(fileReader != null){
                try {
                    fileReader.close();
                } catch (IOException e) {
                    System.out.println(e.getMessage());
                }
            }

        }
    }
}
