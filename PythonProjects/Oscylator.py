import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


def get_chart(x0, y0, time, h, a, b):
    all_x = []
    all_y = []
    x_prior = x0
    y_prior = y0
    for i in range(0, len(time)):
        x = x_prior + h*y_prior
        y = y_prior + h*(-b*x-a*y_prior)
        all_x.append(x_prior)
        all_y.append(y_prior)
        x_prior = x
        y_prior = y
    return all_x, all_y



T, t0, x0, y0, h = 20, 0, 2, 0, 0.01
alpha,beta  = 0.1, 1.0
time = np.arange(t0, T, h).tolist()
line1, line2 = get_chart(x0, y0, time, h,alpha ,beta)

fig = plt.figure()
fig2 = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig2.add_subplot(111)


#wykresy (xt) (yt)
ax1.plot(time, line1, color = 'b', label = ' - x')
ax1.plot(time, line2, color = 'r', label = ' - y')
ax1.set_xlabel('czas')
ax1.set_ylabel('')
ax1.set_title("model oscylator")
ax1.legend(loc = 'best')


line12, line22 = get_chart(3, 1.5, time, h,alpha ,beta )
line13, line23 = get_chart(5, 2, time, h,alpha ,beta )
line14, line24 = get_chart(9, 4, time, h,alpha ,beta )
line15, line25 = get_chart(12, 6, time, h,alpha ,beta )

#wykresy 3d
fig3 = plt.figure()
ax4 = fig3.add_subplot(111, projection = '3d')
ax4.plot(line1, line2, time)

ax4.scatter(line1[0], line2[0], time[0], c = 'g', label = 'start [0,2]')
ax4.scatter(line1[len(line1) - 1], line2[len(line1) - 1], time[len(line1) - 1], c = 'r', label = 'end [0,2]')

ax4.plot(line12,line22,time)
ax4.scatter(line12[0], line22[0], time[0], label = 'start [3,1.5]')
ax4.scatter(line12[len(line12) - 1], line22[len(line12) - 1], time[len(line12) - 1], label = 'end [3,1.5]')


ax4.plot(line13,line23,time)
ax4.scatter(line13[0], line23[0], time[0],  label = 'start [5,2]')
ax4.scatter(line13[len(line13) - 1], line23[len(line13) - 1], time[len(line13) - 1],  label = 'end [5,2]')
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
ax2.set_title("xy-Model Oscylator")
ax2.legend(loc = 'best')

ax1.grid()
ax2.grid()

ax4.grid()


plt.show()