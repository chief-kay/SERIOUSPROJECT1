from math import cos, sin, pi
import numpy
points = [[2, 3, 7], [6, 6 ,7], [1, 0, 2]]
axisx = [1, 0, 0]
axisy = [0, 1, 0]
axisz = [0, 0, 1]
axes = [axisx, axisy, axisz]
rotx = 90
roty = 0
rotz = 0
origin = [0, 0, 0]
matrixrotx = numpy.array([[1,0,0],[0,cos(rotx*pi/180),-sin(rotx*pi/180)],[0,sin(rotx*pi/180),cos(rotx*pi/180)]])
matrixroty = numpy.array([[cos(roty*pi/180),0,-sin(roty*pi/180)],[0,1,0],[sin(roty*pi/180),0,cos(roty*pi/180)]])
matrixrotz = numpy.array([[cos(rotz*pi/180),-sin(rotz*pi/180),0],[sin(rotz*pi/180),cos(rotz*pi/180),0],[0,0,1]])
new_points = []
for point in points:
    point = numpy.array(point)
    new_point_x = numpy.matmul(matrixrotx, point)
    new_point_xy = numpy.matmul(matrixroty, new_point_x)
    new_point_xyz = numpy.matmul(matrixrotz, new_point_xy)
    new_points.append(new_point_xyz.tolist())
print(new_points)