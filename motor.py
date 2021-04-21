import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName=jointName
        self.robot = p.loadURDF("body.urdf")

    def Set_Value(self):
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg
        targetAngles=numpy.linspace(-numpy.pi , numpy.pi, 1000)
        self.motorValues=self.amplitude * numpy.sin(self.frequency * targetAngles + self.offset)

        pyrosim.Set_Motor_For_Joint(
        bodyIndex = self.robot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition =  self.motorValues,
        maxForce = 40)

    # def Save_Values(self):
        # numpy.save('data/targetAngles.npy', targetAngles)
        # numpy.save('data/motorValuesBack.npy', motorValuesBack)
        # numpy.save('data/motorValuesFront.npy', motorValuesFront)