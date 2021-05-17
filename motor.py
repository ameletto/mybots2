from numpy.lib.shape_base import take_along_axis
import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg

        self.motorValuesBack = self.amplitude * numpy.sin(self.frequency * numpy.linspace(-numpy.pi , numpy.pi, 1000) + self.offset)
        self.motorValuesFront = self.amplitude * numpy.sin(self.frequency * numpy.linspace(-numpy.pi , numpy.pi, 1000) + self.offset)
        print(self.motorValuesBack)

    def Set_Value(self):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = p.loadURDF("body.urdf"),
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.motorValuesBack,
        maxForce = 40)

    # def Save_Values(self):
        # numpy.save('data/motorValuesBack.npy', motorValuesBack)
        # numpy.save('data/motorValuesFront.npy', motorValuesFront)