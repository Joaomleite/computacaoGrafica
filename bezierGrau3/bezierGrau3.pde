float p1x = 100;
float p1y = 300;
float p2x;
float p2y;
float p3x = 300;
float p3y= 100;
float p4x = 700;
float p4y = 300;

void setup()
{
  size(800,600);
}

void createBezierPoints(){
  
  float p2x = mouseX;
  float p2y = mouseY;

  for(float t = 0; t <= 1; t += 0.01)
  {
    //Criacao do Ponto A
    float ax = p1x + t*(p2x-p1x);
    float ay = p1y + t*(p2y-p1y);
    
    //Criacao do Ponto B
    float bx = p2x + t*(p3x-p2x);
    float by = p2y + t*(p3y-p2y);
    
    //Criacao do Ponto C
    float cx = p3x + t*(p4x-p3x);
    float cy = p3y + t*(p4y-p3y);
    
    //Criacao do Ponto D
    float dx = ax + t*(bx - ax);
    float dy = ay + t*(by - ay);
    
    //Criacao do Ponto E
    float ex = bx + t*(cx - bx);
    float ey = by + t*(cy - by);
     
    //Criacao do Ponto F
    float fx = dx + t*(ex - dx);
    float fy = dy + t*(ey - dy);
    vertex(fx,fy);  
  }
}

void draw()
{
  background(128);
  beginShape();
  vertex(p1x, p1y);
  createBezierPoints();
  vertex(p4x, p4y);
  endShape(CLOSE);
}
