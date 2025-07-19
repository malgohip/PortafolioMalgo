public class NumeroComplejo{
    public int re, im;
    public NumeroComplejo(){re = 1;im = 1;}
    public NumeroComplejo(int r, int i){re = r; im = i;}
    public void print(){System.out.println(this + ":\t" + re + "+" + im + "i");}
}