
void setup(){
  size(600,600);
}

void drawSun(){
   fill(255, 200, 50);
   translate(width/2, height/2);
   circle(0,0,64);
}

void drawEarth(){
  rotate(frameCount/(10*TWO_PI));
  translate(150,0);
  fill(50, 200, 255);
  circle(0,0,32);
}

void drawMoon(){
  rotate(frameCount/TWO_PI);
  translate(36,0);
  fill(255, 255, 255);
  circle(0,0,12);
}

void draw() {
  
  background(255);  
  drawSun();
  
  pushMatrix();
  drawEarth();
    
  pushMatrix();
  
  drawMoon();
  
  popMatrix();
  
  popMatrix();

}
