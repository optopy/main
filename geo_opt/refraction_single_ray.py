import numpy as np
import matplotlib.pyplot as plt


def propagation(inRay=np.zeros([2, 1]), d=0, n=1):
    rayTransferMatrix = np.array([[1, d/n], [0, 1]])
    outRay = rayTransferMatrix.dot(inRay)
    return outRay

def refraction(inRay=np.zeros([2, 1]), n1=1, n2=1, r=np.inf):
    rayTransferMatrix = np.array([[1, 0], [-(n2-n1)/(n2*r), n1/n2]])
    outRay = rayTransferMatrix.dot(inRay)
    return outRay


n_1 = 1  # Refractive index of incidence medium
n_2 = 1.5  # Refractive index of refraction medium
inPlane = .3  # Longitudinal position of the boundry (in meters)

inHeight = .2  # ray height at the input plane
inAngleDeg = 60  # incident angle in degrees
inAngle = inAngleDeg*(np.pi/180)  # incident angle in radian

ray_1 = np.array([[inHeight], [inAngle]])


fig = plt.figure()
ax = fig.add_subplot()
plt.axis([0, 1, 0, 1])
plt.xlabel('z(m)')
plt.ylabel('y(m)')
plt.grid()

# First medium
rect1 = plt.Rectangle((inPlane, 0), 1-inPlane, 1, color='r', alpha=.4)
ax.add_patch(rect1)
# Second medium
rect2 = plt.Rectangle((0, 0), inPlane, 1, color='b', alpha=.4)
ax.add_patch(rect2)


ray_2 = propagation(ray_1, inPlane)
ray_3 = refraction(ray_2, n_1, n_2)
ray_4 = propagation(ray_3, 1-inPlane, n_2)

plt.plot([0, inPlane, 1], [ray_1[0], ray_2[0], ray_4[0]], color='w')
# plt.xlim((0,1))
# plt.ylim((0,1))
plt.show()

