import matplotlib.pyplot as plt
import numpy

# Import sensor data
data = numpy.genfromtxt("imuFactorExampleResults.csv", delimiter=",", skip_header=1)

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')

estimate_position = data[:, 1:4]
gt_position = data[:, 8:11]

esti_x = estimate_position[:,0]
esti_y = estimate_position[:,1]
esti_z = estimate_position[:,2]

gt_x = gt_position[:,0]
gt_y = gt_position[:,1]
gt_z = gt_position[:,2]

ax.plot(esti_x,esti_y, esti_z,'-', label="estimate position",linewidth =2)
ax.plot(gt_x,gt_y, gt_z,'--', label="GT position")

# Set axes label
ax.set_xlabel('x', labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)

ax.set_title('IMU Factor Example Results')
plt.legend()
plt.show()
