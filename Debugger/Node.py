class Node:
    def __init__(self, d = None):
        self.data = d
        self.next = None
        self.previous = None
        
    def setData(self, e):
        self.data = e

    def getData(self):
        return(self.data)

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious

    def getNext(self):
        return(self.next)
    
    def getPrevious(self):
        return(self.previous)
    
    def __str__(self):
        return(str(self.getData()))