//6. Haga una aproximación del valor de $\pi$, usando como referencia el Ejemplo 2 de la sección 3.5.3. Para este ejercicio, agrege a la imagen del ejemplo 2 una circunferencia centrada en el punto $C(200,200)$ y de radio $r = 200$ y permita que el código calcule el número de puntos que caen dentro de la circunferencia. Use la relación $$\frac{A(C)}{A(R)} \approx \frac{\text{Numero de puntos dentro de circunferencia}}{\text{Numero total de puntos}}  $$ donce $A(C)=\pi r^2$ y $A(R) = 200\times 200$.

let puntos_dentro = 0
let puntos_totales = 0

function setup(){
    createCanvas(500, 500);
    background(255);
    stroke(0);
    ellipse(200, 200, 400, 400);
}

function draw(){
    PuntosRandomPi()
}

function PuntosRandomPi(){
    if (puntos_totales < 1000){
        x = random(0, 400);
        y = random(0, 400);
        distancia_x = x - 200;
        distancia_y = y - 200;
        distancia_centro = (distancia_x ** 2 + distancia_y ** 2) ** 0.5;
        if (distancia_centro <= 200){
            stroke(0, 255, 0);
            puntos_dentro += 1;
        }
        else{
            stroke(255,0,0);
            
        }
        point(x, y);
        puntos_totales += 1;
    }
    else{
        pi_aproximado = 4*(float(puntos_dentro) / float(puntos_totales));
        print("Aproximacion de pi:", pi_aproximado);
        print("Proceso terminado");
    }
    
}