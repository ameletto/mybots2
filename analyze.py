import numpy
import matplotlib.pyplot

backLegSensorValues=numpy.load('backLegSensorValues.npy') 
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)

matplotlib.pyplot.show()