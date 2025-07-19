/*function setup(){
    createCanvas(500,500);
}
function draw(){
    background("#f1faee");
    //rectangulo azul plomo
    fill("#264653")
    rect(50, 50, 200, 400);
    //rectàngulo verde
    fill("#2a9d8f")
    rect(250, 50, 200, 200);
    //rectangulo amarillo
    fill("#e9c46a")
    rect(250, 250, 100, 100);
    //rectangulo naranja ligero
    fill("#f4a261")
    rect(350, 250, 100, 100);
    //rectangulo naranja claro
    fill("#e76f51")
    rect(250, 350, 100, 100);
    //rectangulo naranja fuerte
    fill("#e15f3f")
    rect(350, 350, 100, 100);
}*/

/*let nb = 20; //nb corresponde al nùmero de circulos.
let dim = 0; //dim corresponde al diametro del cìrculo. Posteriormente lo modificamos
let margen = 20; //corresponde al margen en pixeles.
let f = 0 // variable que guarda el seno de un àngulo
let frecuencia = 1;

function setup(){
    createCanvas(500, 500);
    dim = (width - 2*margen)/nb; // calculamos el diametro para ajustarlo al ancho de la ventana
    angleMode(DEGREES); //Trabajo los angulos en grados.
 }
function draw(){
    background(0); //fondo negro
    stroke(255); //figuras sin bordes
    noFill(); //figuras llenas de blanco
    //A continuaciòn un doble for para pintar la grilla de cìrculos
    f = sin(frameCount);
    for( let j = 0; j < nb; ++j)
      for(let i = 0; i < nb ; ++i)
      {
        x = margen + dim/2 + i*dim;
        y = margen + dim/2 + j*dim
        f = sin(frecuencia*frameCount + dist(width/2,height/2,x,y));
        circle(x, y, f*dim);
      }

}*/

/*let nb = 20; //nb corresponde al nùmero de circulos.
let dim = 0; //dim corresponde al diametro del cìrculo. Posteriormente lo modificamos
let margen = 20; //corresponde al margen en pixeles.
let f = 0 // variable que guarda el seno de un àngulo
let frecuencia = 1;

function setup(){
    createCanvas(500, 500);
    dim = (width - 2*margen)/nb; // calculamos el diametro para ajustarlo al ancho de la ventana
    angleMode(DEGREES); //Trabajo los angulos en grados.
 }
function draw(){
    background(0); //fondo negro
    stroke(255); //figuras sin bordes
    noFill(); //figuras llenas de blanco
    //A continuaciòn un doble for para pintar la grilla de cìrculos
    f = sin(frameCount);
    for( let j = 0; j < nb; ++j)
      for(let i = 0; i < nb ; ++i)
      {
        x = margen + dim/2 + i*dim;
        y = margen + dim/2 + j*dim
        f = sin(frecuencia*frameCount + dist(mouseX,mouseY,x,y));
        circle(x, y, f*dim);
      }

}*/

/*let nb = 10; //nb corresponde al nùmero de circulos.
let dim = 0; //dim corresponde al lado del cuadrado. Posteriormente lo modificamos
let margen = 40; //corresponde al margen en pixeles.
let x, y;

function setup(){
    createCanvas(500, 500);
    dim = (width - 2*margen)/nb; // calculamos el diametro para ajustarlo al ancho de la ventana
    noLoop(); //Permite que la función draw se ejecute solamente vez.
 }
function draw(){
    background(255); //fondo blanco
    for( let j = 0; j < nb; ++j)
      for(let i = 0; i < nb ; ++i)
      {
        x = margen + i*dim;
        y = margen + j*dim

        noFill();
        stroke(100,100,220);
        rect(x,y,dim,dim);
        stroke(0);

        let rnd = int(random(0,4));//Elige números enteros del 0 al 4.
        fill(50,100,255);
        if (rnd == 0 )
          triangle(x, y, x + dim, y + dim,x+dim,y);
        
        else if (rnd == 1)
          triangle(x, y, x + dim, y + dim,x,y+dim);
        
        else if (rnd == 2)
          triangle(x, y, x, y + dim,x+dim,y);
        
        else
          triangle(x+dim, y+dim, x+dim, y,x,y+dim);
        
      }
}*/

let nb = 360;
let dim = 300;
let rot = 3;
let f = 0.5;

function setup(){
  createCanvas(500,500);
  rectMode(CENTER);
  angleMode(DEGREES);
}
function draw(){
  background(0);
  translate(width/2, height/2);
  noFill();
  stroke(255);
  for (let i = 0; i < nb; ++i){
    square(0,0,f*dim);
    rotate(rot);
  }
}