class mixed extends fraction{
    int ent, res;
    public mixed(int n, int d){super (n,d); ent=num/den; res=Math.abs(num%den);}
    public String toString(){String concat=""; if (res==0) concat+=ent; else{ if (ent==0) concat+=super.toString(); else concat+=ent+" "+res+"/"+den;} return concat;}
}