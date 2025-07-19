let size = 1000;
let i = 0;

function setup() {
  createCanvas(size, size);  // Define el lienzo con ancho y alto de 'size'
  background(0);  // Establece el fondo negro
}

function draw() {
  stroke(255,0,0);

  if (i <= width / 4) {
    millis(200);
    line(0, 0 + i, width / 4 - i, 0);
    line(i + width / 4, 0, width / 2, 0 + i);
    line(width / 2, 0 + i, 3 * width / 4 - i, 0);
    line(3 * width / 4 + i, 0, width, 0 + i);
  }
  
  if (i <= size) {
    millis(200);
    line(0, width / 10 + i, 0 + i, width);
    line(width / 10 + i, width, width, width - i);
    i += 10;
  }
}