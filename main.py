from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Load configuration settings from file
        self.config = ConfigParser()
        self.config.read('config.ini')
        
        # Load level data
        self.level1 = self.loader.loadModel('level1.bam')
        self.level2 = self.loader.loadModel('level2.bam')
        
        # Set up camera and lighting
        self.disableMouse()
        self.camera.setPos(0, 0, 10)
        self.light = self.render.attachNewNode(PointLight("light"))
        self.light.setPos(0, 0, 10)
        self.render.setLight(self.light)
        
        # Set up key bindings
        self.accept('escape', self.quit)
        
    def quit(self):
        self.cleanup()
        self.userExit()
        
    def cleanup(self):
        pass
        
game = Game()
game.run()
