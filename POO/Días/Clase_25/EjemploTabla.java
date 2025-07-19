/*import javax.swing.*;

public class EjemploTabla extends JFrame {
    public void ActionPerformed(ActionEvent ae){
        System.out.println("Works");
    }

    public EjemploTabla() {
        setTitle("Tabla de medalleria juegos olimpicos Tokyo 2020");
        String[] encabezados = {"Pais", "Oro", "Plata", "Bronce"};
        String[][] valores = {
            {"China", "29", "17", "16"},
            {"Estados Unidos", "22", "25", "17"},
            {"Japón", "17", "6", "10"}
        };
        JTable table = new JTable(valores, encabezados);
        JScrollPane jsp = new JScrollPane(table);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        JPanel contenido = new JPanel();
        contenido.setLayout(new GridLayout(5,1));
        JButton boton = new JButton("Add Column");
        boton.addActionListener(this);
        contenido.add(jsp);
        contenido.add(boton);
        add(contenido);
        pack();
        setVisible(true);
    }

    public static void main(String[] args) {
        new EjemploTabla();
    }
}
*/