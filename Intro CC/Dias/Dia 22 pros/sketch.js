/*function setup() {
  createCanvas(500, 500);
}

function draw() {
  background(220);
}*/

/*function setup() {
    createCanvas(500, 500);
  }
  
  function draw() {
    background(220);
    point(250, 250);
    line(100, 0, 250, 150);
    rect(300, 50, 100, 100);
    ellipse(250, 300, 100, 50);
  }*/

/*function setup(){
    createCanvas(500,500);
  }
function draw(){
   for (let i=0;i<510; i+=10 )
      line(500-i,0,0,i);
  }*/

/*function setup() {
    createCanvas(400, 400);
  }
  
function draw() {
    background(200, 100, 50);
  }*/

/*function setup() {
  createCanvas(500, 500);
  }
function draw(){
    stroke(255,0,0);
    rect(200,200,100,100);
    stroke(0,255,0);
    ellipse(250,250,80,40);
    stroke(0,0,255);
    point(250,250);
  }*/

/*function setup() {
  createCanvas(500, 500);
}
function draw(){
    background(200, 100, 50);
    ellipse(200,200,mouseX,mouseY);
}*/

/*let contador = 1;
function setup() {
  createCanvas(500, 500);
}
function draw(){
    PuntosRandom();
}
function PuntosRandom(){
        stroke(255,0,0); //Permite pintar los puntos con color rojo
        if (contador  <= 1000)
        {
             let X=  random(20,380);
             let Y=  random(20,380);
             let temporizador=millis();
             point(X, Y);
             contador +=1;
        }
        else
        {
             print("Proceso Terminado...\n");
             noLoop();
        }
}*/

/*let contador = 1;
function setup() {
  createCanvas(500, 500);
}
function draw(){
    PuntosRandom();
}


function PuntosRandom(){

        strokeWeight(10); //aumenta el diametro del punto pintado en 10 pixels
        if (contador  <= 1000)
        {
             let Rojo =  random(0,255);  //Se elijen los tonos de los colores rojo, verde y azul de manera aleatoria.
             let Verde = random(0,255);
             let Azul =  random(0,255);
             stroke(Rojo,Verde,Azul);
             let X= random(20,380);
             let Y= random(20,380);
             let temporizador=millis();
             point(X, Y);
             contador +=1;
        }
        else
        {
             print("Proceso Terminado...\n");
             noLoop();
        }
}*/

/*let i = 0;
function setup(){
    createCanvas(500, 500);
    background(255); // Blanco para el fondo de la ventana
}

function  draw(){
    Segmentos();
}

function Segmentos(){
        stroke(255,0,0);
        if (i  <= 500)
        {
             let temporizador=millis();
             line(500-i,0,0,i);
             temporizador=millis();
             i +=10;
        }
        else
        {
             print("Proceso Terminado...\n");
             noLoop();
        }
}*/

function setup(){
  createCanvas(500, 500);
}
function draw(){
  background(255);
  fill(0); //llena con negro el interior de las figuras
  noStroke(); // elimina los bordes de las figuras
  if (mouseX < width/3){
      rectMode(CENTER); // rectMode es una funciòn que el modo del comando square
                        // en este caso la referencia serà las coordenadas del
                        // centro de la ventana.
      square(width/2, height/2, 400);
  }
  else if (mouseX < 2*width/3){
      circle(width/2, height/2, 400);
  }
  else{
      triangle(250,50,450,450,50,450);
  }
}