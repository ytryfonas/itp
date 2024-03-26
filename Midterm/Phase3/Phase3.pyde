def setup():
    size(710, 510)
    background(255)
    stroke(100)

def drawObject(x,y,s):
    push()
    translate(x, y)
    scale(s)
    ellipse(35, 30, 70, 40) # face
    ellipse(20, 25, 20, 10) # left eye
    ellipse(50, 25, 20, 10) # right eye
    fill(0)
    ellipse(20, 25, 6, 10) # left iris
    ellipse(50, 25, 6, 10) # right iris
    noFill()
    line(10, 0, 30, 10) # left ear
    line(10, 0, 30, 10)
    line(10, 0, 0, 30)
    line(60, 0, 70, 30) # right ear
    line(60, 0, 40, 10)
    line(30, 30, 40, 30) # nose
    line(30, 30, 35, 40)
    line(40, 30, 35, 40) 
    line(30, 36, 5, 30) # whiskers
    line(30, 40, 5, 36)
    line(40, 36, 65, 30)
    line(40, 40, 65, 36)
    pop()
    
def draw():
    drawObject(100,200,1.8)
    drawObject(352,200,1.8)
    drawObject(200,100,2.5)
    

    
