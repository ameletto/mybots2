from numpy.lib.shape_base import take_along_axis
import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName, robot):
        self.jointName = jointName
        self.theRobot = robot
        # self.Prepare_To_Act()

    # def Prepare_To_Act(self):
    #     self.amplitude = c.amplitudeBackLeg
    #     self.frequency = c.frequencyBackLeg
    #     self.offset = c.phaseOffsetBackLeg
    #     if self.jointName == "Torso_FrontLeg":
    #         self.motorValues = self.amplitude * numpy.sin(self.frequency/2 * numpy.linspace(-numpy.pi , numpy.pi, 1000) + self.offset)
    #     else:
    #         self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(-numpy.pi , numpy.pi, 1000) + self.offset)

    def Set_Value(self, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = self.theRobot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = 40)

    # def Save_Values(self):
    #     numpy.save('data/motorValues.npy', self.motorValues)