import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

amplitudeBackLeg=numpy.pi/4
frequencyBackLeg=10
phaseOffsetBackLeg=numpy.pi/4

amplitudeFrontLeg=numpy.pi/4
frequencyFrontLeg=10
phaseOffsetFrontLeg=0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAngles=numpy.linspace(-numpy.pi , numpy.pi, 1000)
motorValuesBack=amplitudeBackLeg * numpy.sin(frequencyBackLeg * targetAngles + phaseOffsetBackLeg)
motorValuesFront=amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * targetAngles + phaseOffsetFrontLeg)
numpy.save('data/targetAngles.npy', targetAngles)
numpy.save('data/motorValuesBack.npy', motorValuesBack)
numpy.save('data/motorValuesFront.npy', motorValuesFront)


for i in range (1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition =  motorValuesBack[i],
    maxForce = 40)
    
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = motorValuesFront[i],
    maxForce = 40)

    time.sleep(1/500)
p.disconnect()
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
