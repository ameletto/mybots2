import pybullet as p
import pybullet_data
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

import robot

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
        # targetAngles=numpy.linspace(-numpy.pi , numpy.pi, 1000)
        # motorValuesBack=c.amplitudeBackLeg * numpy.sin(c.frequencyBackLeg * targetAngles + c.phaseOffsetBackLeg)
        # motorValuesFront=c.amplitudeFrontLeg * numpy.sin(c.frequencyFrontLeg * targetAngles + c.phaseOffsetFrontLeg)

        # numpy.save('data/targetAngles.npy', targetAngles)
        # numpy.save('data/motorValuesBack.npy', motorValuesBack)
        # numpy.save('data/motorValuesFront.npy', motorValuesFront)

        for t in range (1000):
            p.stepSimulation()
            self.robot.Sense(t)

            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robot,
            # jointName = "Torso_BackLeg",
            # controlMode = p.POSITION_CONTROL,
            # targetPosition =  motorValuesBack[i],
            # maxForce = 40)

            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robot,
            # jointName = "Torso_FrontLeg",
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = motorValuesFront[i],
            # maxForce = 40)

            time.sleep(1/1000) 

    def __del__(self):
        p.disconnect()

        # numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
        # numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
