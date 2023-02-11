#need of a reference point... normli Cg / origin
#presentation of objects in points. 
#pionts, (2 2 1) (3 2 1) (1 2 3)
dx = 67
dy = 56
dz = 10
points = [[2, 2, 3], [3, 2, 1], [1, 2, 3]]
point0 = points[0] 
point1 = points[1]
point2 = points[2]
point0x = point0[0]
point0y = point0[1]
point0z = point0[2]
point1x = point1[0]
point1y = point1[1]
point1z = point1[2]
point2x = point2[0]
point2y = point2[1]
point2z = point2[2]
point0x = point0x + dx
point1x = point1x + dx
point2x = point2x + dx
point0y = point0y + dy
point1y = point1y + dy
point2y = point2y + dy
point0z = point0z + dz
point1z = point1z + dz
point2z = point2z + dz
points = [[point0x, point0y, point0z], [point1x, point1y, point1z], [point2x, point2y, point2z]]




dx = 67
dy = 56
dz = 54
points = [[2, 2, 3], [3, 2, 1], [1, 2, 3]]
point0 = points[0] 
point1 = points[1]
point2 = points[2]
point0x = point0[0] + dx
point0y = point0[1] + dy
point0z = point0[2] + dz
point1x = point1[0] + dx
point1y = point1[1] + dy
point1z = point1[2] + dz
point2x = point2[0] + dx
point2y = point2[1] + dy
point2z = point2[2] + dz
points = [[point0x, point0y, point0z], [point1x, point1y, point1z], [point2x, point2y, point2z]]
print(points)

dx = 3
dy = 2
dz = 1
points = [[2, 2, 3], [3, 2, 1], [1, 2, 3]]
for point in points:
    point[0] = point[0] + dx
    point[1] = point[1] + dy
    point[2] = point[2] + dz
print(points)

dx = 3
dy = 2
dz = 1
points = [[2, 2, 3], [3, 2, 1], [1, 2, 3]]
points = [[p[0]+dx, p[1]+dy, p[2]+dz] for p in points]
print(points)

import numpy
dx = 3
dy = 2
dz = 1
points = numpy.array([[2, 2, 3], [3, 2, 1], [1, 2, 3]]) + numpy.array([dx, dy, dz])
print(points)