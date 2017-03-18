# swimfishclass.py
# Assignment 9: Swimming Fish via Classes
# Cathy Lee
# Input: User enters a number
# Output: Graphics window with aquarium drawn

from graphics import *
from random import *

class MovingFish:
    def __init__(self,x,y,color,speed,dist):
        self.speed = speed
        p1 = Point(x-(dist*10),y)
        p2 = Point(x-(dist*16),y+12)
        p3 = Point(x-(dist*16),y-12)
        self.tail = Polygon(p1,p2,p3)
        p4 = Point(x+15,y+8)
        p5 = Point(x-15,y-8)
        self.ovbody = Oval(p4,p5)
        p6 = Point(x+(dist*6),y+2)
        self.eye = Circle(p6,2)
        p7 = Point(x+(dist*7),y+2)
        self.eye2 = Circle(p7,1)
        p8 = Point(x,y-2)
        self.fin = Circle(p8,2.5)
        p9 = Point(x+(dist),y-2)
        self.fin2 = Circle(p9,2.5)
        self.fin2.setOutline(color)
        
    def setFill(self,color):
        self.tail.setFill(color)
        self.ovbody.setFill(color)
        self.eye.setFill('white')
        self.eye2.setFill('black')
        self.fin.setFill(color)
        self.fin2.setFill(color)

    def getSpeed(self):
        return self.speed

    def getCenter(self):
        return self.ovbody.getCenter()

    def move(self,dx,dy):
        self.tail.move(dx,dy)
        self.ovbody.move(dx,dy)
        self.eye.move(dx,dy)
        self.eye2.move(dx,dy)
        self.fin.move(dx,dy)
        self.fin2.move(dx,dy)

    def draw(self,win):
        self.tail.draw(win)
        self.ovbody.draw(win)
        self.eye.draw(win)
        self.eye2.draw(win)
        self.fin.draw(win)
        self.fin2.draw(win)

def RandColor(nfish):
    
    '''Generates a color for the fish.
    '''
    
    Lcolor = []
    for k in range(nfish):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        color = color_rgb(r,g,b)
        Lcolor.append(color)
    return Lcolor

def FishCoords(nfish):
    
    '''Generates coordinates for the fish.
    '''
    
    Lcoords = []
    for i in range(nfish):
        x = randint(-100,100)
        y = randint(-70,100)
        Lcoords.append([x,y])
    return Lcoords

def Speeds(nfish):
    
    '''Creates a list of speeds to parallel to the disks.
    '''
    
    Lspeeds = []
    maxspeed = 2
    
    for x in range(nfish):
        x = randint(-maxspeed,maxspeed)
        # Remove 0 from list of speeds
        while x == 0:
            x = randint(-maxspeed,maxspeed)
        Lspeeds.append(x)
    return Lspeeds

def Offset(nfish,Lspeeds):
    
    '''Determines offset between body parts (eye & tail)
    and the coordinates of the centre of the body.
    '''
    
    # Initialise base distance value for coordinates fish body parts
    dist = 1
    Ldist = []
    
    # Determine position of body parts according to +/-ve speed
    for speed in Lspeeds:
        if speed > 0:
            Ldist.append(dist)
        else:
            Ldist.append(-dist)
    return Ldist

def drawFish(win,nfish):
    
    '''Draws fish.
    '''
    
    Lcolor = RandColor(nfish)
    Lcoords = FishCoords(nfish)
    Lspeeds = Speeds(nfish)
    Ldist = Offset(nfish,Lspeeds)

    Lfish = []
    
    for i in range(nfish):
        x = Lcoords[i][0]
        y = Lcoords[i][1]
        fish = MovingFish(x,y,Lcolor[i],Lspeeds[i],Ldist[i])
        # Draw fish
        fish.setFill(Lcolor[i])
        fish.draw(win)
        Lfish.append(fish)
    return Lfish

def Movement(Lfish,Lspeeds):
    
    '''Moves and wraps fish around graphics window.
    '''
    
    for i in range(len(Lfish)):
        f = Lfish[i]
        speed = f.getSpeed()
        f.move(speed, 0)
        point = f.getCenter()
        # Wrap fish around window
        x = point.getX()
        if x > 100:
            f.move(-200,0)
        elif x < -100:
            f.move(200,0)

#------------------------------------------------

class Sandbed:
    def __init__(self,r2,x2,y2):
        p1 = Point(101,-80)
        p2 = Point(-101,-101)
        self.bed = Rectangle(p1,p2)
        self.bed.setFill('light goldenrod')
        self.bed.setOutline('light goldenrod')
        self.r2 = r2
        p3 = Point(x2,y2)
        self.sw = Circle(p3,r2)
        self.sw.setFill('sea green')
        self.sw.setOutline('sea green')
        
    def draw(self,win):
        self.bed.draw(win)
        self.sw.draw(win)

def SeaweedCoords():

    '''Creates 4 sets of coordinates for the seaweed.
    '''
    
    Lswcoords = []
    for x in range(-75,95,45):
        for y in range(-78,-60,5):
            x2 = x
            y2 = y
            Lswcoords.append([x2,y2])
    return Lswcoords

def drawSand(win):

    '''Draws sandbed.
    '''
    
    r2 = 3
    Lswcoords = SeaweedCoords()
    for i in range(len(Lswcoords)):
        x2 = Lswcoords[i][0]
        y2 = Lswcoords[i][1]
        sand = Sandbed(r2,x2,y2)
        sand.draw(win)

#------------------------------------------------

class MovingSquid:
    def __init__(self,x3,y3,speed):
        self.x3 = x3
        self.y3 = y3
        self.speed = speed
        p1 = Point(x3+20,y3+20)
        p2 = Point(x3-20,y3-20)
        self.sbody = Rectangle(p1,p2)
        self.sbody.setFill('light slate blue')
        self.sbody.setOutline('light slate blue')
        p3 = Point(x3+20,y3+25)
        p4 = Point(x3+20,y3-25)
        p5 = Point(x3+30,y3)
        self.shead = Polygon(p3,p4,p5)
        self.shead.setFill('light slate blue')
        self.shead.setOutline('light slate blue')
        p6 = Point(x3-20,y3+20)
        p7 = Point(x3-30,y3+18)
        self.stail = Rectangle(p6,p7)
        self.stail.setFill('light slate blue')
        self.stail.setOutline('light slate blue')
        p8 = Point(x3-20,y3+2)
        p9 = Point(x3-30,y3)
        self.stail2 = Rectangle(p8,p9)
        self.stail2.setFill('light slate blue')
        self.stail2.setOutline('light slate blue')
        p10 = Point(x3-20,y3-18)
        p11 = Point(x3-30,y3-20)
        self.stail3 = Rectangle(p10,p11)
        self.stail3.setFill('light slate blue')
        self.stail3.setOutline('light slate blue')
        p12 = Point(x3+10,y3+10)
        r = 4
        self.topeye = Circle(p12,r)
        self.topeye.setFill('black')
        p13 = Point(x3+10,y3-10)
        self.bottomeye = Circle(p13,r)
        self.bottomeye.setFill('black')
        p14 = Point(x3-10,y3)
        self.mouth = Circle(p14,6)
        self.mouth.setFill('indian red')
        self.mouth.setOutline('indian red')
        p15 = Point(x3-4,y3+6)
        p16 = Point(x3-10,y3-6)
        self.cover = Rectangle(p15,p16)
        self.cover.setFill('light slate blue')
        self.cover.setOutline('light slate blue')

    def getCenter(self):
        return self.sbody.getCenter()

    def move(self,dx,dy):
        self.x3 = self.x3+dx
        self.y3 = self.y3+dy
        self.sbody.move(dx,dy)
        self.shead.move(dx,dy)
        self.stail.move(dx,dy)
        self.stail2.move(dx,dy)
        self.stail3.move(dx,dy)
        self.topeye.move(dx,dy)
        self.bottomeye.move(dx,dy)
        self.mouth.move(dx,dy)
        self.cover.move(dx,dy)

    def getSpeed(self):
        return self.speed

    def getCenter(self):
        return self.sbody.getCenter()

    def draw(self,win):
        self.sbody.draw(win)
        self.shead.draw(win)
        self.stail.draw(win)
        self.stail2.draw(win)
        self.stail3.draw(win)
        self.topeye.draw(win)
        self.bottomeye.draw(win)
        self.mouth.draw(win)
        self.cover.draw(win)

def SquidCoords():

    '''Generates random coordinates for the squid.
    '''
    
    x3 = randint(-100,100)
    y3 = randint(-50,50)
    return x3,y3

def drawSquid(win):

    '''Draws the squid.
    '''
    
    x3,y3 = SquidCoords()
    squid = MovingSquid(x3,y3,randint(1,5))
    squid.draw(win)
    return squid

def SquidMovement(squid):

    '''Moves the squid.
    '''
        
    speed = squid.getSpeed()
    squid.move(speed,0)
    # Wrap squid around graphics window
    point = squid.getCenter()
    x = point.getX()
    if x > 100:
        squid.move(-200,0)
    elif x < -100:
        squid.move(200,0)
        
#------------------------------------------------

def main():
    
    '''A program that draws an aquarium.
    '''
    
    win = GraphWin('Aquarium',600,600)
    win.setBackground('cornflower blue')
    w = 100
    win.setCoords( -w, -w, w, w)

    drawSand(win)
    nfish = eval(input('Fill the aquarium with this number of fish: '))
    print('Number of fish:',nfish)
    Lspeeds = Speeds(nfish)
    print('Fish speeds:',Lspeeds)

    print('-----------------------------------------------')
    Lfish = drawFish(win,nfish)
    print('Click for a new tank addition!')
    win.getMouse()
    squid = drawSquid(win)

    print('Click to make the fish move.')
    # User clicks to start animation
    win.getMouse()
    while True:
        # User clicks to stop animation
        if win.checkMouse():
            break
        Movement(Lfish,Lspeeds)
        SquidMovement(squid)

    print('Click to stop movement.')
    
    print('Click again to close.')
    win.getMouse()
    win.close()


main()

