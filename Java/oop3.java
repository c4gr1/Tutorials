public class oop3 {

    private int x;
    private int y;
    private int uzunluk;

    public int getX(){
        return x;
    }

    public void setX(int _x){
        if(_x >= 0){
            x = _x;
        }
        else{
            System.out.println("x -1 den buyuk olmalı");
        }
    }

    public int getY(){
        return y;
    }

    public void setY(int _y){
        if(_y >= 0){
            y = _y;
        }
        else{
            System.out.println("y -1 den buyuk olmalı");
           
        }
    }

    public int getU(){
        return uzunluk;
    }

    public void setU(int _u){
        if(_u >= 0){    
            uzunluk = _u;
        }
        else{
            System.out.println("uzunluk -1 den buyuk olmalı");
        } 
    }

    public void ekranaBastir(){
        System.out.println("X: " + x);
        System.out.println("Y: " + y);
        System.out.println("Uzunluk: " + uzunluk);
    }
    
}
