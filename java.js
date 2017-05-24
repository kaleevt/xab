
//Auto starts the game
function startGame() {
    myGameArea.start();
}


//Game area Canvas
var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 480;
        this.canvas.height = 270;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
    }
}


// Varifying Object e.g. the monster or thing to destroy
var myGamePiece;

function startGame() {
    myGameArea.start();
    
    
    //In colour area put link to image 
    myGamePiece = new component(30, 30, "image.jpg", 10, 120, 'image');
}

//Think this is the game piece appearance and location
function component(width, height, color, x, y) {
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;    
    ctx = myGameArea.context;
    ctx.fillStyle = color;
    ctx.fillRect(this.x, this.y, this.width, this.height);
}
