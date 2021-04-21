import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName=linkName
        self.values = numpy.zeros(1000)

    def Get_Value(self, i, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(i)
        # if t==99:
        #     # print(self.values)

    # def Save_Values(self):
    #     numpy.save('data/sensorValues.npy', self.values)




