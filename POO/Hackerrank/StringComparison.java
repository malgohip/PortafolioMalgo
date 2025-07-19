public class StringComparison {
    public static boolean areStringsEqual(String str1, String str2) {
        // Usar el método equals para comparar los strings
        if (str1 == null || str2 == null) {
            return false; // Si alguno es null, no son iguales
        }
        return str1.equals(str2);
    }

    public static void main(String[] args) {
        // Ejemplo de uso
        String string1 = "US: $12,324.13\r\n" + //
                        "India: Rs.12,324.13\r\n" + //
                        "China: ￥12,324.13\r\n" + //
                        "France: 12 324,13 €";
        String string2 = "US: $12,324.13\r\n" + //
                        "India: Rs.12,324.13\r\n" + //
                        "China: ￥12,324.13\r\n" + //
                        "France: 12 324,13 €";

        boolean result = areStringsEqual(string1, string2);
        System.out.println("¿Son iguales? " + result);
    }
}