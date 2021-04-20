import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.motors = MOTOR()
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        ROBOT.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = SENSOR()
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)
