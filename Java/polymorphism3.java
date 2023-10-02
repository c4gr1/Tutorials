public class polymorphism3 extends polymorphism{

    public void openConnection(){
        System.out.println("MsSQL bağlantısı açıldı");
    }

    public void closeConnection(){
        System.out.println("MsSQL bağlantısı kapatıldı");
    }

    public void executeQuery(String sql){
        System.out.println("MsSQL komutları çalıştırıldı");
    } 
    
}
