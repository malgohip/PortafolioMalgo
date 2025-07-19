public class fraction {
    
    public int num,den,cos,res;

    public fraction(){this(0,1,0,0);}

    public fraction(int num1, int den1, int cos1, int res1){num=num1;den=den1;cos=cos1;res=res1;}
    
    public fraction(fraction p){this(p.num,p.den,p.cos,p.res);}

    public void neg(){if (num<0 ^ den<0){if (cos==0) {num=Math.abs(num); den=Math.abs(den); res=num%den*-1; num*=-1;} else{num=Math.abs(num);den=Math.abs(den);cos=num/den; res=num%den; cos*=-1;num*=-1;}} else{num=Math.abs(num); den=Math.abs(den); cos=Math.abs(cos); res=Math.abs(res);}}

    public void printprop(){if (den==1) System.out.print(num);else System.out.print(num+"/"+den);}

    public void printmxt(){if (cos==0){System.out.print(res+"/"+den);} else{if(res==0){System.out.print(cos);}else{System.out.print(cos+" "+res+"/"+den);}}}

    public fraction diference(fraction b){int nnum=(num*b.den)-(b.num*den), nden=den*b.den; return new fraction(nnum,nden,nnum/nden,nnum%nden);}

    public fraction division(fraction b){int numdiv=(num*b.den), dendiv=(den*b.num); fraction divi = new fraction(numdiv,dendiv,numdiv/dendiv,numdiv%dendiv); return divi;}
    
    public fraction simplfier(){int MCD=mcd(num,den); while (MCD!=1){num/=MCD; den/=MCD; MCD=mcd(num,den);}fraction simpli = new fraction(num,den,num/den,num%den);return simpli;}

    public fraction addition(fraction b){int nnum=((num*b.den)+(b.num*den)), nden=den*b.den; return new fraction(nnum,nden,nnum/nden,nnum%nden);}

    public static int mcd(int num1, int num2){int a = Math.max(num1, num2), b = Math.min(num1, num2), res = 0; while (b != 0){res = b; b = a % b; a = res;} return res;}
}