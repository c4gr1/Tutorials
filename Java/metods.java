import java.util.Scanner;

public class metods{
    public static void main(String[] args) {
        
        //  program1();

        //  new metods().program2();

        //  float sonuc = new metods().program3(1.2f,7);
        //  System.out.println(sonuc);

        //  metods Methods = new metods();
        //  Methods.program4();

    }

//  Static-Static olmayan fonksiyon çağrısı mainde farklı

    public static void program1(){

        System.out.println("Hello World");
        System.out.println(Math.pow(2,3));
        System.out.println(Math.sqrt(16));

        Scanner scanner = new Scanner(System.in);
        String nextLine = scanner.nextLine();
        System.out.println(nextLine.toUpperCase());

        scanner.close();

    }

    public void program2(){

        System.out.println("Hello World");

    }

    public int program3(int x,int y){

        int toplam = x + y;
        return toplam;

    }

    public float program3(float x,int y){

        float toplam = x + y;
        return (float)toplam;

    }

    public void program4(){

        System.out.println("hello");

    }

}
