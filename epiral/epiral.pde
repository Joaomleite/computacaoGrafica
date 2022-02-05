void setup() {
  size(400, 400);
  frameRate(10);
}

void draw() {
  background(255);
  int n = (frameCount * 50);  
  translate(width/2, height/2);
  noStroke();
  fill(0);
  
  beginShape();
  for (int i = 0; i < n; i++) {
    float t = radians(i);
    
    float x = 2 * t * cos(t);
    float y = 2 * t * sin(t);
    
    ellipse(x, y, 2, 2);
  }
  endShape();
}
