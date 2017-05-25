color[] palette = {#8B4513, #006400, #90EE90, #A0522D, #228B22};

void setup () {
 size (600,500);
 smooth();
 noFill();
 strokeWeight(3);
 frameRate(50);
 background(palette[0]);
}

void draw () {
 float x = random(width);
 float y = random(height);
 float d = random(80,300);
 stroke(palette[int(random(1,5))]);
 rect(x,y,d,d); 
}