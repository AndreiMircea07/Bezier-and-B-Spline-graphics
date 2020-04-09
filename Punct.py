class Punct:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def getX(self):
        
        return self.x
    
    def getY(self):
            
        return self.y
    
    def setX(self):
        
        return self.x
    
    def setY(self):
        
        return self.y    
    
    def __str__(self):
        return str(self.x)+' '+str(self.y)
    