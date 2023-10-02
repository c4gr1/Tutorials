//Renge göre filtrelemek için oluşturulan sınıf arayüzü kullanır

public class interfaces3 implements interfaces2{

    @Override
    public boolean filtrele(interfaces elma){
        return elma.getRenk().equals("Kırmızı");
    }
    
}
