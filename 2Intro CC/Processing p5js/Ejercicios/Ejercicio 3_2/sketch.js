//3. Diseñe el código para obtener las siguientes figuras usando solo el comando `line`.
//![texto alternativo](https://drive.google.com/uc?id=1l1SfOpbFYqACXyr3M6ZlZ4_PDrxQ4Nch)

function setup(){
  createCanvas(500, 500);
  background(200); // Blanco para el fondo de la ventana
}

function  draw(){
  for (let i=0;i<510; i+=10 ){
    line(0+i,0,0,250-i);
    line(250+i,0,500,0+i);
    line(0,250+i,0+i,500);
    line(250+i,500,500,500-i);
  }
}
