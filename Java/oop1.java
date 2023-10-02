public class oop1 {

    public String marka;
    public oop1_Kalemtipi tip;
    public boolean doldurulabilir;
    public boolean silinebilir;

    public void yaz(String metin){
        System.out.println(metin);
    }

    public void tekrarDoldur(){
        if(doldurulabilir){
            System.out.println("kalem dolduruldu");
        }
        else{
            System.out.println("bu kalem doldurulamaz");
        }
    }

    public void sil(){
        if(silinebilir){
            System.out.println("yazı silindi");
        }
        else{
            System.out.println("bu yazı silinemez");
        }
    }

}
