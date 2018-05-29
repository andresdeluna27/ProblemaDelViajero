import random
import math
class Ciudad(object):
    num=0
    def __init__(self,numero):
        self.num=numero
        self.x=None
        self.y=None
        #self.x=random.randint(0,15)
        #self.y=random.randint(0,15)
        if self.num==1:
            self.x=5;
            self.y=4;
        elif self.num==2:
            self.x=7;
            self.y=4;
        elif self.num==3:
            self.x=5;
            self.y=6;
        elif self.num==4:
            self.x=4;
            self.y=3; 
        elif self.num==5:
            self.x=3;
            self.y=6;
        elif self.num==6:
            self.x=4;
            self.y=5;
        elif self.num==7:
            self.x=2;
            self.y=4;
        elif self.num==8:
            self.x=1;
            self.y=3;
        elif self.num==9:
            self.x=1;
            self.y=5;
        elif self.num==10:
            self.x=3;
            self.y=2;
        elif self.num==11:
            self.x=6;
            self.y=3;
        elif self.num==12:
            self.x=7;
            self.y=7;
        elif self.num==13:
            self.x=6;
            self.y=1;
        elif self.num==14:
            self.x=4;
            self.y=1;
        elif self.num==15:
            self.x=1;
            self.y=1;
        elif self.num==16:
            self.x=1;
            self.y=7;
        elif self.num==17:
            self.x=4;
            self.y=7;
        elif self.num==18:
            self.x=7;
            self.y=2;
        elif self.num==19:
            self.x=9;
            self.y=2; 
        elif self.num==20:
            self.x=8;
            self.y=5;
        elif self.num==21:
            self.x=10;
            self.y=4;
        elif self.num==22:
            self.x=11;
            self.y=1;
        elif self.num==23:
            self.x=10;
            self.y=7;
        elif self.num==24:
            self.x=13;
            self.y=6;
        elif self.num==25:
            self.x=12;
            self.y=8;    
        
    def distancia(self, city):
        return float(math.sqrt(math.pow((self.x-city.x),2)+math.pow((self.y-city.y),2)))

    def impr(self):
        return str("x: "+str(self.x)+" y: "+str(self.y))

    def getNum():
        return int(self.num)
        
        
        
    
