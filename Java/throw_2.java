//  istisna sınıfı throw için

//  public class throw_2 extends RuntimeException{} kullanırsak eğer throw_java
//  dosyasındaki fonksiyon parametresi sonrasında throws kelimesini kullanmamız
//  gerekmez  
public class throw_2 extends Exception {

    public throw_2(String degiskenAdi, Object deger){
        super(degiskenAdi +" " + deger + " olamaz!");
    }

}
