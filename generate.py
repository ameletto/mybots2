import pyrosim.pyrosim as pyrosim

x=0.5
y=0.5
z=0.5

length=1
width=1
height=1

pyrosim.Start_SDF("world.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

"""
for i in range (6):
    y=y+1
    x=1
    for j in range (6):
        length=1
        width=1
        height=1
        z=0.5
        x=x+1
        for k in range (10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            length=length*0.9
            width=width*0.9
            height=height*0.9
            z=z+height
"""
pyrosim.End()

