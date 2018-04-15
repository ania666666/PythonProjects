import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#x - prey
#y - predator
def lorentzFun(x,y,z):
    x_dot = 10.0 * (y - x)
    y_dot = 28.0 * x - y - x * z
    z_dot = x * y - (8.0 / 3.0) * z
    return x_dot, y_dot, z_dot

def get_chart(x0, y0,z0, time, h):
    x = []
    y = []
    z=[]
    xi = x0
    yi = y0
    zi=z0
    for i in time:
        x.append(xi)
        y.append(yi)
        z.append(zi)
        x_dot, y_dot, z_dot = lorentzFun(xi, yi, zi)
        xi += h * x_dot
        yi += h * y_dot
        zi += h * z_dot


    return x,y,z



T, t0, x0, y0,z0, h = 40., 0., 1.0, 1.0,1.0, 0.01
alpha,beta  = 0.1, 1.0
time = np.arange(t0, T, h)
line1, line2,line3 = get_chart(x0, y0, z0,time, h)

fig = plt.figure()
fig2 = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig2.add_subplot(111)


#wykresy (xt) (yt)
ax1.plot(time, line1, color = 'b', label = ' - x')
ax1.plot(time, line2, color = 'r', label = ' - y')
ax1.set_xlabel('czas')
ax1.set_ylabel('')
ax1.set_title("model lorentza")
ax1.legend(loc = 'best')


line12, line22,line32 = get_chart(3, 1.5,0.75 ,time, h )
line13, line23,line33 = get_chart(5, 2,1, time, h )
line14, line24,line34 = get_chart(9, 4,2, time, h )
line15, line25,line35 = get_chart(12, 6,3, time, h)

#wykresy 3d
fig3 = plt.figure()
ax4 = fig3.add_subplot(111, projection = '3d')
ax4.plot(line1, line2, line3,c='violet')

ax4.scatter(line1[0], line2[0], time[0], c = 'g', label = 'start [0,2]')
ax4.scatter(line1[len(line1) - 1], line2[len(line1) - 1], line3[len(line1) - 1], c = 'pink', label = 'end [0,2]')

ax4.plot(line12,line22,line32,c='fuchsia')
ax4.scatter(line12[0], line22[0], time[0], label = 'start [3,1.5]')
ax4.scatter(line12[len(line12) - 1], line22[len(line12) - 1], line32[len(line12) - 1],c='violet', label = 'end [3,1.5]')


ax4.plot(line13,line23,line33,c='crimson')
ax4.scatter(line13[0], line23[0], time[0],  label = 'start [5,2]')
ax4.scatter(line13[len(line13) - 1], line23[len(line13) - 1], line33[len(line13) - 1],  label = 'end [5,2]')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.legend(loc = 'best')

##wykresy (xy)

ax2.plot(line1, line2, color = 'pink', label = '(1, 0.5)')

ax2.plot(line12, line22, color = 'violet', label = '(3, 1.5)')
ax2.plot(line13, line23, color = 'fuchsia', label = '(5, 2)')
ax2.plot(line14, line24, color = 'deeppink', label = '(9, 4)')
ax2.plot(line15, line25, color = 'crimson', label = '(12, 6)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title("xy-Model Lorentza")
ax2.legend(loc = 'best')

ax1.grid()
ax2.grid()

ax4.grid()

plt.show()