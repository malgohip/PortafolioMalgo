import java.util.*;

abstract class MetaHuman{
    protected String nombre; protected int vida; protected int dagno;
    public MetaHuman(String nome, int lif, int dam){nombre=nome; vida=lif; dagno=dam;}
    public boolean dead(){return vida<=0;}
    public void getdam(int damage){vida-=damage;}
    public String getNombre(){return nombre;}
    public int getVida(){return vida;}
}

class Hero extends MetaHuman{
    private int creditos; private int cantAumentarVida=2; private int cantDuplicarAtaque=2;
    public Hero(String name, int live, int damage, int credits){super(name, live, damage); creditos=credits;}
    public void Atack(Villain villano){if (!(dead())){villano.getdam(dagno); System.out.println(villano.getNombre()+" recibe "+dagno+" puntos de dano. Vida restante: "+villano.getVida());}}
    public void UseSpecial(String special){
        if (dead()) return;
        switch (special) {
            case "aumentar_vida": if(cantAumentarVida>0){cantAumentarVida--; vida+=50; System.out.println(nombre+" aumenta su vida. Vida actual: "+vida);} else System.out.println("No tienes mas habilidades disponibles, debes comprar. Perdiste el turno."); break;
            case "duplicar_ataque": if(cantDuplicarAtaque>0){cantDuplicarAtaque--; dagno*=2; System.out.println(nombre+" duplica su ataque. Ataque actual: "+dagno);} else System.out.println("No tienes mas habilidades disponibles, debes comprar. Perdiste el turno."); break;
            default: System.out.println("Habilidad no valida. Perdiste el turno."); break;
        }
    }
    public void BuySpecial(String special){
        if (dead()) return;
        switch (special) {
            case "aumentar_vida": if(creditos>=40){cantAumentarVida++; creditos-=40; System.out.println("Has comprado la habilidad aumentar_vida");} else System.out.println("No tienes los suficientes creditos para comprar esta habilidad. Perdiste el turno."); break;
            case "duplicar_ataque": if(creditos>=20){cantDuplicarAtaque++; creditos-=20; System.out.println("Has comprado la habilidad duplicar_ataque");} else System.out.println("No tienes los suficientes creditos para comprar esta habilidad. Perdiste el turno."); break;
            default: System.out.println("Habilidad no valida. Perdiste el turno."); break;
        }
    }
}

class Villain extends MetaHuman{
    public Villain(String name, int live, int damage){super(name, live, damage);}
    public void Atack(Hero heroe){if (!(dead())){heroe.getdam(dagno); System.out.println(heroe.getNombre()+" recibe "+dagno+" puntos de dano. Vida restante: "+heroe.getVida());}}
}

public class HeroesvsVillanos{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String Herosname = sc.nextLine(); int Heroeslive = sc.nextInt(), Heroesdamage = sc.nextInt(), Heroescredits = sc.nextInt(); sc.nextLine(); Hero bueno = new Hero(Herosname, Heroeslive, Heroesdamage, Heroescredits);
        String Villainsname = sc.nextLine(); int Villainslive = sc.nextInt(), Villainsdamage = sc.nextInt(); sc.nextLine(); Villain malo = new Villain(Villainsname, Villainslive, Villainsdamage); 
        System.out.println("Comienza la batalla\n" + bueno.getNombre()+": Vida = "+bueno.getVida()+"\n"+malo.getNombre()+": Vida = "+malo.getVida());
        while(!(bueno.dead())&&!(malo.dead())&&sc.hasNext()){
            if (sc.hasNextInt()){int action = sc.nextInt();
                switch (action) {
                    case 1: bueno.Atack(malo); break;
                    case 2: if (sc.hasNext()){String hability = sc.next(); bueno.UseSpecial(hability);} break;
                    case 3: if (sc.hasNext()){String hability = sc.next(); bueno.BuySpecial(hability);} break;
                    default: System.out.println("Opcion invalida. Perdiste el turno."); break;
                }
            }
            else {System.out.println("Entrada no valida. Perdiste el turno."); sc.next();}
            if (!(malo.dead())) malo.Atack(bueno);
        }
        if (bueno.dead()) System.out.println("El heroe ha sido derrotado.");
        else System.out.println("Has derrotado al villano.");
        sc.close();
    }
}