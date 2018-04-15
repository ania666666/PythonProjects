import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


def get_chart(x0, y0, time, h):
    x = []
    y = []
    xi = x0
    yi = y0
    for i in time:
        if i == 0:
            xi = x0
            yi = y0

        else:

            xi = xi + h * (0.04 * xi * xi + 5. * xi + 140. - yi + 30.)

            yi = yi + h * (0.02 * (0.2 * xi - yi))
            if xi > 30.:
                xi = -65.
                yi = yi + 8.

        x.append(xi)
        y.append(yi)
    return  x,y



T, t0, x0, y0, h = 100, 0, -65, 0, 0.01
alpha,beta  = 0.1, 1.0
time = np.arange(t0, T, h).tolist()
line1, line2 = get_chart(x0, y0, time, h)

fig = plt.figure()
fig2 = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig2.add_subplot(111)


#wykresy (xt) (yt)
ax1.plot(time, line1, color = 'b', label = ' - x')
ax1.plot(time, line2, color = 'r', label = ' - y')
ax1.set_xlabel('czas')
ax1.set_ylabel('')
ax1.set_title("model komórki nerwowej")
ax1.legend(loc = 'best')


line12, line22 = get_chart(np.random.randint(0,25),np.random.randint(0,25), time,h)
#line12, line22 = get_chart(3, 1.5, time, h )
line13, line23 = get_chart(np.random.random()*25.,np.random.random()*5, time, h)
line14, line24 = get_chart(np.random.randint(0,25),np.random.randint(0,25), time, h)
line15, line25 = get_chart(np.random.randint(0,25),np.random.randint(0,25), time, h)
n=np.random.rand
#wykresy 3d
fig3 = plt.figure()
ax4 = fig3.add_subplot(111, projection = '3d')
ax4.plot(line1, line2, time)

ax4.scatter(line1[0], line2[0], time[0], c = 'g', label = 'start [-65,0]')
ax4.scatter(line1[len(line1) - 1], line2[len(line1) - 1], time[len(line1) - 1], c = 'r', label = 'end [-65,0]')

ax4.plot(line12,line22,time)
ax4.scatter(line12[0], line22[0], time[0], label = 'start [losowe]')
ax4.scatter(line12[len(line12) - 1], line22[len(line12) - 1], time[len(line12) - 1], label = 'end [losowe]')


ax4.plot(line14,line24,time)
ax4.scatter(line14[0], line23[0], time[0],  label = 'start [lsowe 2]')
ax4.scatter(line14[len(line14) - 1], line24[len(line14) - 1], time[len(line14) - 1],  label = 'end [losowe 2]')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.legend(loc = 'best')

##wykresy (xy)

ax2.plot(line1, line2, color = 'pink', label = '(1, 0.5)')

ax2.plot(line12, line22, color = 'violet', label = '(losowe 1)')
ax2.plot(line13, line23, color = 'fuchsia', label = '(losowe 2)')
ax2.plot(line14, line24, color = 'deeppink', label = '(losowe 3)')
ax2.plot(line15, line25, color = 'crimson', label = '(losowe 4)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title("xy-Model komórki nerwowej")
ax2.legend(loc = 'best')

ax1.grid()
ax2.grid()

ax4.grid()


plt.show()