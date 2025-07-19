//2. Tome de referencia el ejemplo 3 de la sección 3.5.1.  Cree una ventana de 500x500 y use únicamente el comando `line` para construir la figura que se muestra a continuación.
//![texto alternativo](https://drive.google.com/uc?id=1989pUPlPWcS1hG4P5-TTd6cCr9Dz4xoH).

function setup(){
    createCanvas(500, 500);
    background(200); // Blanco para el fondo de la ventana
}

function  draw(){
    for (let i=0;i<510; i+=10 ){
        line(0,0+i,0+i,500)
    }
}