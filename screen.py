import pygame

defaultName = "Screen"
defaultNameNum = 0
defaultW = 20
defaultH = 100
defaultColor = (20, 20, 20)
defaultFlag = pygame.FULLSCREEN

class Screen():
    def __init__(self, name = defaultName, w = defaultW, h = defaultH, color = defaultColor, objects = {}, flag = defaultFlag):
        global defaultNameNum
        if name == defaultName:
            name += " " + str(defaultNameNum)
            defaultNameNum += 1
        self.name = name
        self.wInitial = w
        self.hInitial = h
        self.display = pygame.display.set_mode((self.wInitial, self.hInitial), flags=flag)
        self.displayInfo = pygame.display.Info()
        self.w = self.displayInfo.current_w
        self.h = self.displayInfo.current_h
        self.objects = objects

    def __str__(self) -> str:
        return self.name

    def printSelf(self):
        print("SCREEN PRINT START")
        print(f"Screen Name: {self.name}")
        for attribute in self.__dict__:
            print(f"    {attribute}: {self.__dict__[attribute]}")
        print("SCREEN PRINT END")
    
    def getName(self):
        return self.name
    
    def getW(self):
        return self.w
    
    def getH(self):
        return self.h
    
    def addObjects(self, *args):
        for item in args:
            item.setScreen(self)
            self.objects[item] = item

    def removeObjects(self, *args):
        for item in args:
            if item not in self.objects:
                print(f"Object {item} not found.")
            else:
                del self.objects[item]
                print(f"Object {item} removed succesfully.")

    def update(self, deltaTime, *args):
        if not args:
            for item in self.objects:
                item.update(deltaTime)
        else:
            for item in args:
                item.update(deltaTime)
