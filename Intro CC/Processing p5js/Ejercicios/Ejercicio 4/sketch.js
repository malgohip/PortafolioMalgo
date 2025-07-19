//4. Considere el ejemplo 1 de la sección 3.5.3. Saque el comando   `background(200, 100, 50)` de la función `draw()` y coloquelo como instrucción de la función `setup()`. Observe que la figura que se genera es distinta a la del ejemplo. Explique por qué se presenta esta diferencia en las imagenes.

function setup(){
  createCanvas(400,400);
  background(200, 100, 50);
}
function draw(){
  ellipse(200,200,mouseX,mouseY)
}