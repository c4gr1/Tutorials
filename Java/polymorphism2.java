public class polymorphism2 extends polymorphism {

    public void openConnection(){
        System.out.println("MySQL bağlantısı açıldı");
    }

    public void closeConnection(){
        System.out.println("MySQL bağlantısı kapatıldı");
    }

    public void executeQuery(String sql){
        System.out.println("MySQL komutları çalıştırıldı");
    }    
    
}
