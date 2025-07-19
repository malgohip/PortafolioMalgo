class fraction{

    public int num,den,cos,res;

    public fraction(){this(0,1,0,0);}

    public fraction(int num1, int den1, int cos1, int res1){num=num1;den=den1;cos=cos1;res=res1;}
    
    public fraction(fraction p){this(p.num,p.den,p.cos,p.res);}

    public void neg(){
        if (num<0 ^ den<0){if (cos==0) {num=Math.abs(num); den=Math.abs(den); res=num%den*-1; num*=-1;} else{num=Math.abs(num);den=Math.abs(den);cos=num/den; res=num%den; cos*=-1;num*=-1;}}
        else{num=Math.abs(num);den=Math.abs(den); cos=Math.abs(cos); den=Math.abs(den);}
    }

    public void printprop(){System.out.print(num+"/"+den+" ");}

    public void printmxt(){
        if (cos==0){System.out.print(res+"/"+den+" ");}
        else{if(res==0){System.out.print(cos+" ");}else{System.out.print(cos+" "+res+"/"+den+" ");}}
    }
}