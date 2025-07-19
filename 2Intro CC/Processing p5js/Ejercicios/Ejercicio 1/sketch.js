/*1. Use rectas, rectángulos y elipses para pintar un esquema de un rostro: cabeza, ojos, naríz y boca.*/

function setup(){
  createCanvas(800, 800);
}

function draw(){
    background(255);

    stroke(255, 143, 94);
    strokeWeight(5);
    ellipse(400, 400, 400, 500);
    stroke(0);
    ellipse(320, 320, 100, 60);
    ellipse(480, 320, 100, 60);
    stroke(85, 40, 25);
    ellipse(320, 320, 40, 40);
    ellipse(480, 320, 40, 40);
    stroke(0);
    ellipse(320, 320, 10, 10);
    ellipse(480, 320, 10, 10);
    stroke(255, 143, 94);
    triangle(400, 380, 380, 440,420, 440);
    stroke(255, 0, 0);
    rect(350, 500, 100, 40);
}