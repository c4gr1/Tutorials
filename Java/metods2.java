import java.util.Arrays;

public class metods2 {

    public static int x = 20;

    public static void main(String[] args) {

        metods2 M = new metods2();

        M.normalMetot();

        metods2.staticMetot();

        int max = metods2.max(1, 5, 7);
        System.out.println(max);

        double max2 = metods2.max(1.5, 1.5, 1.7);
        System.out.println(max2);

        boolean majority = metods2.majority(true, false, false);
        System.out.println(majority);

        int[] x = {1,2,3};
        int[] y= {1,2,3};

        boolean eq = metods2.eq(x, y);
        System.out.println(eq);

        int toplam = metods2.toplam(x);
        System.out.println(toplam);

        int[] sonuc = metods2.ciftSayilar(new int[] {1,2,3,4,5,6,7,8,9});
        System.out.println(Arrays.toString(sonuc));

        int x1 = 7;
        int x2 = 77;
        //degistir fonksiyonu işe yaramayacak javada izin verilmiyor 
        degistir(x1, x2);

        System.out.println(x1 + " " + x2);

        int[] dizi = {x1,x2};

        //degistir2 fonksiyonu ile değiştirebiliriz 
        degistir2(dizi);
        
        System.out.println(Arrays.toString(dizi));

    }

    public void normalMetot(){
        System.out.println(x);
    }

    public static void staticMetot(){
        System.out.println(x);
    }

    public static int max(int x,int y,int z){

        int max = x;
        if(y > max)
            max = y;
        if(z > max)
            max = z;

        return max;

    }

    public static double max(double x,double y,double z){

        double max = x;
        if(y > max)
            max = y;
        if(z > max)
            max = z;

        return max;

    }

    public static boolean majority(boolean x, boolean y, boolean z){
        return (x && y) || (x && z) || (y && z);
    }

    public static boolean eq(int[] x, int[] y){

        boolean result = true;

        if(x.length == y.length){

            for(int i=0; i < x.length; i++){
                if(x[i] != y[i]){
                    result = false;
                    break;
                }
            }

        }

        else{
            result = false ;
        }

        return result;

    }

    public static int toplam(int[] x){

        int toplam = 0;

        for(int i=0;i < x.length; i++)
            toplam += x[i];

        return toplam;

    }

    public static int[] ciftSayilar(int[] dizi){

        int[] ciftSayiDizisi = null;
        int j=0;

        for(int i=0; i < dizi.length; i++){

            if(dizi[i] % 2 == 0){;
                j++;
            }
        }

        ciftSayiDizisi = new int[j];
        int k = 0;

        for(int i=0; i < dizi.length; i++){

            if(dizi[i] % 2== 0){;
                ciftSayiDizisi[k++]=dizi[i];
            }
        }       

        return ciftSayiDizisi;

    }

    public static void degistir(int x, int y){
        int temp = x ;
        x = y;
        y = temp ;
    }

    public static void degistir2(int[] dizi){
        int temp = dizi[0];
        dizi[0] = dizi[1];
        dizi[1] = temp;
    }


}