import pyrosim.pyrosim as pyrosim

length=1
width=2
height=3

x=1
y=1
z=1.5

pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
pyrosim.End()