import java.util.*; import java.io.*;

class Mario{
    public int vidas; public int monedas; public String poder;
    public Mario(int lif, int coin, String mirio){vidas=lif; monedas=coin; poder=mirio;}
    public String gana(){if ((vidas>0)&&(monedas>=0)) return "Mario gana"; else return "Mario pierde";}
    public String toString(){return vidas+", "+monedas+", "+poder;}
}

class castillo{
    private int vidas; private int monedas; private ArrayList<String> poderes;
    public castillo(int lifes, int coins, ArrayList<String> powers){vidas=lifes; monedas=coins; poderes=powers;}
    public boolean pasaMario(Mario mario){for (String power: poderes) if (mario.poder.equals(power)) return true; return false;}
    public void pasoMario(Mario mario){mario.vidas-=this.vidas; mario.monedas-=this.monedas;}
    public String toString(){String powers=""; for (String poder: poderes) powers+=poder+", ";return vidas+" \n"+monedas+" \n"+powers.substring(0,powers.length()-2);}
}

public class FUCKMarioBross{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(new File("YaCabronHableBien.txt"));
        HashMap<Integer,String[]> intentos=new HashMap<>();
        for (int i=0; i<5; i++){intentos.put(i,sc.nextLine().split(" ")); if (i<4) sc.nextLine();} sc.close();
        int vidas0 = (Integer.parseInt(intentos.get(0)[1])), monedas0 = (Integer.parseInt(intentos.get(0)[3])); String poder0 = ""; for(int i=5; i<intentos.get(0).length; i++) poder0+=intentos.get(0)[i]+" "; poder0=poder0.substring(0,poder0.length()-1);
        Mario mario = new Mario(vidas0, monedas0, poder0);
        ArrayList<String> poderesBowser = new ArrayList<>(); poderesBowser.add("Super Champinon"); poderesBowser.add("Flor de Fuego"); poderesBowser.add("Estrella de Invencibilidad");
        castillo bowser = new castillo(1,5, poderesBowser); int[] inicial = {1,2,3,4}; ArrayList<int[]> listaPermutaciones = new ArrayList<>(); generarPermutaciones(inicial, 0, listaPermutaciones); String[] ordenCasti = new String[4];
        for (int[] orden: listaPermutaciones){
            HashMap<Integer,Object[]> castillos=new HashMap<>();
            ArrayList<String> poderes0 = new ArrayList<>(); poderes0.add("Super Champinon"); poderes0.add("Estrella de Invencibilidad");
            castillos.put(1, new Object[]{"Ludwig Von Koopa", new castillo(6, 10, poderes0), false});
            ArrayList<String> poderes1 = new ArrayList<>(); poderes1.add("Flor de Fuego"); poderes1.add("Estrella de Invencibilidad");
            castillos.put(2, new Object[]{"Wario", new castillo(9, 20, poderes1), false});
            ArrayList<String> poderes2 = new ArrayList<>(); poderes2.add("Super Capa"); poderes2.add("Hoja de Tanooki"); poderes2.add("Flor de Fuego");
            castillos.put(3, new Object[]{"Lemmy Koopa", new castillo(7, 15, poderes2), false});
            ArrayList<String> poderes3 = new ArrayList<>(); poderes3.add("Super Champinon"); poderes3.add("Hoja de Tanooki"); poderes3.add("Flor de Fuego");
            castillos.put(4, new Object[]{"Iggy Koopa", new castillo(3, 25, poderes3), false});
            mario = new Mario(vidas0, monedas0, poder0); ordenCasti = new String[4];
            for (int i=1; i<5; i++) {
                for (int j : orden){
                    if (!((boolean)castillos.get(j)[2])&&((castillo)castillos.get(j)[1]).pasaMario(mario)){
                    ordenCasti[i-1]=(String)castillos.get(j)[0];
                    castillo casti=((castillo)castillos.get(j)[1]); casti.pasoMario(mario);
                    castillos.get(j)[2]=true; break;
                    }
                }
                    int vidas = (Integer.valueOf(intentos.get(i)[1])), monedas = (Integer.valueOf(intentos.get(i)[3])); String poder = ""; for(int j=5; j<intentos.get(i).length; j++) poder+=intentos.get(i)[j]+" "; poder=poder.substring(0,poder.length()-1);
                    mario.vidas+=vidas; mario.monedas+=monedas; mario.poder=poder;
            }
            if (ordenCasti[3]!=null) break;
        }
        for (String casti: ordenCasti) System.out.println(casti);
        System.out.println("Bowser"); if(bowser.pasaMario(mario)){bowser.pasoMario(mario); System.out.println(mario.gana());} else System.out.println("Mario pierde");
    }
    static void generarPermutaciones(int[] arr, int index, ArrayList<int[]> lista) {if (index == arr.length - 1) {lista.add(arr.clone());return;} for (int i = index; i < arr.length; i++) {swap(arr, index, i); generarPermutaciones(arr, index + 1, lista); swap(arr, index, i);}}
    static void swap(int[] arr, int i, int j) {int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;}
}