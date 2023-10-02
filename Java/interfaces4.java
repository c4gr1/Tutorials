//Ağırlığa göre filtrelemek için oluşturulan sınıf arayüzü kullanır

public class interfaces4 implements interfaces2 {

    @Override
    public boolean filtrele(interfaces elma){
        return elma.getAgirlik() >= 15;
    }
    
}
