public class throw_main {
    public static void main(String[] args) {
        throw_ isci = new throw_();
        
        try {
            isci.setIsim("Kerpeten Ali");
        } catch (throw_2 e) {
            System.out.println(e.getMessage());
        }
        
        try {
            isci.setMaas(-1);
        } catch (throw_2 e) {
            System.out.println(e.getMessage());
            //e.printStackTrace();
        }

        System.out.println(isci);
    }
    
}
