public class interfaces_main {

    public static void main(String[] args) {

        interfaces[] elmalar = new interfaces[10];
        elmalar[0] = new interfaces(10, "Sarı");
        elmalar[1] = new interfaces(20, "Yeşil");
        elmalar[2] = new interfaces(30, "Sarı");
        elmalar[3] = new interfaces(30, "Sarı");
        elmalar[4] = new interfaces(10, "Kırmızı");
        elmalar[5] = new interfaces(20, "Yeşil");
        elmalar[6] = new interfaces(30, "Kırmızı");
        elmalar[7] = new interfaces(10, "Sarı");
        elmalar[8] = new interfaces(20, "Yeşil");
        elmalar[9] = new interfaces(30, "Sarı");

        // yöntem 0 - interface kullanmadan yapılan verimsiz yöntem

        /* 
        renkFiltrele("Kırmızı", elmalar);
        System.out.println("--------------");
        agirlikFiltrele(30, elmalar);
        System.out.println("--------------");
        agirlikFiltrele2(20, elmalar);
        */


        // yöntem 1 - polimorfik çağrım 

        interfaces2 xFiltresi = new interfaces3();
        //interfaces2 xFiltresi = new interfaces4();
        filtrele(xFiltresi, elmalar);

        // yöntem 2 

        /* 
        interfaces3 renkFiltresi = new interfaces3();
        interfaces4 agirlikFiltresi = new interfaces4();
        interfacedeki filtrele değil aşağıdaki filtrele fonksiyonu bu eğer
        neden 2 paremetre aldığını soruyorsan
        filtrele(renkFiltresi, elmalar);
        filtrele(agirlikFiltresi, elmalar);
        */

    }

    public static void filtrele(interfaces2 elmaFiltresi , interfaces[] elmalar){
        for(int i=0;i < elmalar.length; i++){
            interfaces elma = elmalar[i];
            if(elmaFiltresi.filtrele(elma)){
                System.out.println(elma.getAgirlik() + " " + elma.getRenk());
            }
        }


    }
    public static void renkFiltrele(String renk, interfaces[] elmalar){

        for(int i = 0; i<elmalar.length; i++){
            interfaces elma = elmalar[i];

            if(elma.getRenk().equals(renk)){
                System.out.println(elma.getRenk() + " " + elma.getAgirlik());
            }
        }
    }
    public static void agirlikFiltrele(int agirlik, interfaces[] elmalar){

        for(int i = 0; i<elmalar.length; i++){
            interfaces elma = elmalar[i];

            if(elma.getAgirlik() >= agirlik){
                System.out.println(elma.getRenk() + " " + elma.getAgirlik());
            }
        }
    }
    public static void agirlikFiltrele2(int agirlik, interfaces[] elmalar){

        for(int i = 0; i<elmalar.length; i++){
            interfaces elma = elmalar[i];

            if(elma.getAgirlik() < agirlik){
                System.out.println(elma.getRenk() + " " + elma.getAgirlik());
            }
        }
    }

    
}
