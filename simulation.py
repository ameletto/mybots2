import pybullet as p
import pybullet_data
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range (100):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act()
            time.sleep(1/1000) 

    def __del__(self):
        p.disconnect()

        
