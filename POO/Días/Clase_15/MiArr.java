import java.util.*;

public class MiArr {
    private int[] a = {};
    public MiArr(int n){if (n>0){Random generador = new Random(); a = new int[n]; for (int i=0;i<a.length;i++) a[i] = generador.nextInt()%100;}}
    public String toString(){String concat=""; for (int i=0;i<a.length;i++) {concat += a[i] + "\t"; if ((i+1)%10==0) concat += "\n";} return concat;}
    public void invertir(){for (int i=0;i<a.length/2;i++) {int temp=a[i]; a[i]=a[a.length-(i+1)]; a[a.length-(i+1)]=temp;}}
    public int favorito(int f){for (int i=0;i<a.length;i++) if (a[i]==f) return i; return -1;}
    public MiArr hacerEspacio(int fav){int[] arri=new int[a.length+1]; int j = 0; for (int i=0;i<arri.length;i++) {if (i!=fav) {arri[i]=a[j]; j++;} else arri[i]=-1;} MiArr arre = new MiArr(0); arre.a=arri; return (arre);}
    public String busquedaBin(int f){int i = 0, j = a.length-1, mid = (i+j)/2; while (i<=j && f != a[mid]){if (f < a[mid]) j = mid - 1; else i = mid + 1; mid=(i+j)/2;} if (f == a[mid]) return (f+" was found at potition "+ mid); else return (f+" wasn't found");}
    public void ordenBurbuja(){for (int i = 0; i < a.length-1; i++) for (int j = 0; j < a.length-i-1; j++) if (a[j]>a[j+1]){int temp=a[j]; a[j] = a[j+1]; a[j+1] = temp;}}
}