class Nodo {
    Object valor;
    Nodo siguiente;
    Nodo (Object valor) {
        this.valor = valor;
        this . siguiente = null;
    }
}

public class ListaEnlazadaSimple {
    class ListaSimple {
        private Nodo cabeza; private int n=0;

        void insertarInicio(int valor){
            Nodo nuevo = new Nodo (valor); nuevo.siguiente = cabeza; cabeza = nuevo; n++; return;
        }

        void insertarFinal(int valor){
            Nodo nuevo = new Nodo (valor); 
            if (cabeza==null){cabeza = nuevo; n++; return;}
            Nodo t = cabeza; while (t.siguiente != null) t=t.siguiente;
            t.siguiente=nuevo; n++; return;
        }

        void eliminarInicio(){
            if (cabeza == null) return; cabeza = cabeza.siguiente; n--; return;
        }

        void eliminarFinal(){
            if (cabeza == null) return;
            if (cabeza.siguiente == null) {cabeza=null; n--; return;}
            Nodo t = cabeza; while (t.siguiente != null) t=t.siguiente;
            t.siguiente=null; n--; return;
        }

        void insertarEnPosicion(int pos, Object valor) {
            Nodo aux = cabeza, nuevo = new Nodo (valor); int indice = 0;
            if (pos == 0) {nuevo.siguiente = cabeza; cabeza = nuevo; return;}
            while (aux != null && indice < pos - 1) {aux = aux.siguiente; indice++;}
            nuevo.siguiente = aux.siguiente; aux.siguiente = nuevo; n++;
        }

        void insertarAntesDe(Object referencia, Object valor){
            Nodo temp = cabeza; int pos = 0; while (temp != null){
                if (temp.valor.equals(referencia)){
                    Nodo aux = cabeza, nuevo = new Nodo (valor); int indice = 0; 
                    if (pos==0) {nuevo.siguiente = cabeza; cabeza = nuevo; return;}
                    while (aux != null && indice < pos-1) {aux = aux.siguiente; indice++;}
                    nuevo.siguiente = aux.siguiente; aux.siguiente = nuevo; return;
                }
                temp = temp.siguiente; pos++; 
            } n++;
        }

        void eliminarPorValor(Object valor) {
            Nodo aux = cabeza;
            while (aux.siguiente != null){
                if (aux.siguiente.valor.equals(valor)) {aux.siguiente = aux.siguiente.siguiente; return;}
                aux = aux.siguiente;
            } n--;
        }

        void eliminarEnPosicion(int pos){
            if (pos==0){cabeza = cabeza.siguiente; return;}
            Nodo aux = cabeza; int indice = 0;
            while (aux != null && indice < pos-1) {aux = aux.siguiente; indice++;}
            aux.siguiente = aux.siguiente.siguiente; n--;
        }

        void imprimir(){
            Nodo temp = cabeza;
            while (temp != null){
                System.out.print(temp.valor + " -> ");
                temp = temp.siguiente;
            }
            System.out.println("null");
        }

        public int tamagno() {return n;}
    }
}
