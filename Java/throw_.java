//  isci sınıfını tutan sınıf

public class throw_ {

    private String isim;
    private double maas;

    public String getIsim(){
        return isim;
    }
    
    public void setIsim(String isim) throws throw_2{
        if(isim == null || isim.trim().length() == 0){
            throw new throw_2("isim", isim);
        }
        this.isim = isim;
    }

    public double getMaas(){
        return maas;
    }

    public void setMaas(double maas)throws throw_2{
        if(maas < 0){
            throw new throw_2("maas", maas);
        }
        this.maas = maas;
    }

    @Override
    public String toString() {
        
        return "İsim: " + isim + ", Maaş: " + maas;
    }


}
