import numpy
import matplotlib.pyplot

# backLegSensorValues=numpy.load('data/backLegSensorValues.npy') 
# frontLegSensorValues=numpy.load('data/frontLegSensorValues.npy')
# matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth=2)
# matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg')

targetAngles=numpy.load('data/targetAngles.npy')
matplotlib.pyplot.plot(targetAngles, numpy.sin(targetAngles))
matplotlib.pyplot.xlabel('Angle [rad]')
matplotlib.pyplot.ylabel('sin(x)')

matplotlib.pyplot.show()