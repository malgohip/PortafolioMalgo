//5. Rediseñe el programa de los ejercicios 2. y 3. usando el comando `millis()` con el fin tener una construcción dinámica de las figuras.

let i = 0
function setup(){
  createCanvas(500, 500);
  background(255);
}

function draw(){
  //segmentos_1();
  //segmentos_2();
  //circulo();
}

function segmentos_1(){
  stroke(0)
  if (i  <= 500){
    millis(200);
    line(0,0+i,0+i,500);
    i +=10;
  }
  else{
    print("Proceso Terminado...\n");
    noLoop();
  }
}

function segmentos_2(){
  stroke(0)
  if (i  <= 500){
    millis(200);
    line(0+i,0,0,500-i);
    line(0,0+i,500-i,500);
    line(0+i,0,500,500-i);
    i +=10;
  }
  else{
    print("Proceso Terminado...\n");
    noLoop();
  }
}

function circulo(){
  stroke(0)
  if (i  <= 500){
    millis(200);
    line(0+i,0,0,250-i);
    line(250+i,0,500,0+i);
    line(0,250+i,0+i,500);
    line(250+i,500,500,500-i);
    i +=10;
  }
  else{
    print("Proceso Terminado...\n");
    noLoop();
  }
}