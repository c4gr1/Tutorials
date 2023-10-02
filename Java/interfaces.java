//  Elmalar hakkında bilgi tutan sınıf

public class interfaces {
    
    private int agirlik;
    private String renk;

    public interfaces(int agirlik, String renk){
        this.agirlik = agirlik;
        this.renk = renk;
    }

    public int getAgirlik(){
        return agirlik;
    }

    public void setAgirlik(int agirlik){
        this.agirlik = agirlik;
    }

    public String getRenk(){
        return renk;
    }

    public void setRenk(String renk)
    {
        this.renk = renk;
    }
}
