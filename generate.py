import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x1,y1,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length,width,height])
    pyrosim.End()

x=0
y=0
z=0.5

x1=-3
y1=3

length=1
width=1
height=1

Create_World()
Create_Robot()

# for i in range (6):
#     y=y+1
#     x=1
#     for j in range (6):
#         length=1
#         width=1
#         height=1
#         z=0.5
#         x=x+1
#         for k in range (10):
#             pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#             length=length*0.9
#             width=width*0.9
#             height=height*0.9
#             z=z+height

