PImage img;

void setup () {
 size (1000,500);
 smooth();
 noFill();
 strokeWeight(3);
 frameRate(10);
 background(51);
 img = loadImage("tree.png");

}

void draw () {
 float x = random(width);
 float y = random(height);
 float d = random(80,300);
 image(img,x,y,d,d); 

}
