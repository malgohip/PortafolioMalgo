class fraction{
    public int num,den;
    public fraction(int num1, int den1){num=num1; den=den1; if (den<0){num*=-1; den*=-1;} }
    public String toString(){return num+"/"+den;}
}