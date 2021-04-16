import pyrosim.pyrosim as pyrosim

length=1
width=1
height=1

x=1
y=1
z=0.5

x2=2
y2=1
z2=1.5

pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])
pyrosim.End()