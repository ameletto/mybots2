import numpy
import matplotlib.pyplot

# backLegSensorValues=numpy.load('data/backLegSensorValues.npy') 
# frontLegSensorValues=numpy.load('data/frontLegSensorValues.npy')
# matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth=2)
# matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg')

motorValues=numpy.load('data/motorValues.npy')
matplotlib.pyplot.plot(motorValues, label='Motor Values')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()