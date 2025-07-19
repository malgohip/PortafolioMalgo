class Sports{
    String getName(){return "Generic Sports";}
    void getNumberOfTeamMembers(){System.out.println( "Each team has n players in " + getName() );}
}

class Soccer extends Sports{
    @Override String getName(){return "Soccer Class";}
    @Override void getNumberOfTeamMembers(){System.out.println( "Each team has 11 players in " + getName() );}
}

public class N18_Java_Method_Overriding {
    
    public static void main(String[] args) {
        System.out.println("Generic Sports"); Sports general = new Sports(); general.getNumberOfTeamMembers(); 
        System.out.println("Soccer Class"); Sports soccer = new Soccer(); soccer.getNumberOfTeamMembers(); 
    }
}