public class polymorphism {

    public void openConnection(){
        System.out.println("Veritabanı bağlantısı açıldı");
    }

    public void closeConnection(){
        System.out.println("Veritabanı bağlantısı kapatıldı");
    }

    public void executeQuery(String sql){
        System.out.println("SQL komutları çalıştırıldı");
    }

}
