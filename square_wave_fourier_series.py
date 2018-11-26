import numpy as np
import pylab as py

order = 1000

theta = np.arange(2*order*100+1)/(2*order*100.)  * 2 * np.pi
square_wave = np.concatenate((np.ones(order*100), -np.ones(order*100+1)))

py.clf()
py.plot(theta, square_wave, 'k-', linewidth=2)
py.ylim((-1.5,1.5))
py.xlim((0,4.))
py.savefig('sqaure_wave_order_0.png')
total = np.zeros(len(theta))
for i in range(1,order,2):
    new = 4./np.pi/i * np.sin(i*theta)
    total += new
    py.clf()
    py.plot(theta, square_wave, 'k-', linewidth=2)
    py.plot(theta, new, 'r-', linewidth=2)
    py.ylim((-1.5,1.5))
    py.xlim((0,4.))
    py.plot(theta, total, 'b-', linewidth=2)
    py.savefig('square_wave_order_'+str(i)+'.png')
