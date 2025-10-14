class NodoDoble {
    Object valor;
    NodoDoble siguiente;
    NodoDoble anterior;
    NodoDoble (Object valor) {
        this.valor = valor;
        this.siguiente = null;
        this.anterior = null;
    }
}

public class ListaEnlazadaDoble {
    class ListaDoble {
        private NodoDoble cabeza; private NodoDoble cola; private int n=0;

        void insertarInicio(int valor){
            NodoDoble nuevo = new NodoDoble(valor);
            if (cabeza==null){cabeza=cola=nuevo; n++; return;}
            nuevo.siguiente = cabeza; cabeza.anterior = nuevo; cabeza = nuevo;
            n++;
        }

        void insertarFinal(int valor){
            NodoDoble nuevo = new NodoDoble (valor); 
            if (cabeza==null){cabeza=cola=nuevo; n++; return;}
            nuevo.anterior = cola; cola.siguiente = nuevo; cola = nuevo;
            n++;
        }

        void eliminarInicio(){
            if (cabeza == null) return; cabeza = cabeza.siguiente; n--; return;
        }

        void eliminarFinal(){
            if (cola == null) return; cola = cola.anterior; n--; return;
        }

        void insertarEnPosicion(int pos, Object valor) {
            NodoDoble aux = cabeza, nuevo = new NodoDoble (valor); int indice = 0;
            if (pos == 0) {nuevo.siguiente = cabeza; cabeza = nuevo; n++; return;}
            while (aux != null && indice < pos - 1) {aux = aux.siguiente; indice++;}
            nuevo.siguiente = aux.siguiente; aux.siguiente = nuevo; n++;
        }

        void insertarAntesDe(Object referencia, Object valor){
            NodoDoble temp = cabeza; int pos = 0; while (temp != null){
                if (temp.valor.equals(referencia)){
                    NodoDoble aux = cabeza, nuevo = new NodoDoble (valor); int indice = 0; 
                    if (pos==0) {nuevo.siguiente = cabeza; cabeza = nuevo; n++; return;}
                    while (aux != null && indice < pos-1) {aux = aux.siguiente; indice++;}
                    nuevo.siguiente = aux.siguiente; aux.siguiente = nuevo; n++; return;
                }
                temp = temp.siguiente; pos++; 
            }
        }

        void eliminarPorValor(Object valor) {
            NodoDoble aux = cabeza;
            if (cabeza.valor.equals(valor)) {cabeza = cabeza.siguiente; n--; return;}
            while (aux.siguiente != null){
                if (aux.siguiente.valor.equals(valor)) {aux.siguiente = aux.siguiente.siguiente; n--; return;}
                aux = aux.siguiente;
            } 
        }

        void eliminarEnPosicion(int pos){
            if (pos==0){cabeza = cabeza.siguiente; return;}
            NodoDoble aux = cabeza; int indice = 0;
            while (aux != null && indice < pos-1) {aux = aux.siguiente; indice++;}
            aux.siguiente = aux.siguiente.siguiente; n--;
        }

        void imprimir(){
            NodoDoble temp = cabeza;
            while (temp != null){
                System.out.print(temp.valor + " -> ");
                temp = temp.siguiente;
            }
            System.out.println("null");
        }

        void imprimirInverso(){
            if (cola == null) return;
            NodoDoble temp = cola;
            while (temp != null){
                System.out.print(temp.valor + " -> ");
                temp = temp.anterior;
            }
            System.out.println();
        }

        public int tamagno() {return n;}
    }
}
