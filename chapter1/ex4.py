from matplotlib.pylab import *
import numpy as np

v = 0                                                   
t_total = 0                                          
s = [] 
t = []
def caculate():
    global s0,s,t_total,v,t
    print 'please inut initial position'
    s0 = int(raw_input())                     
    print 'please input  initial  velocity. '
    v = float(raw_input())                 
    print 'please input time used through the jourey.'
    t_total = float(raw_input())        
    print 'please input time step'
    dt = float(raw_input())                
    print 'please input a'
    a = float(raw_input())                           
    for i in range(int(t_total/dt)):
        ti = dt*i
        si =s0 +v*dt*i+0.5*a*(ti**2)
        t.append(ti)
        s.append(si)
        print t[-1],s[-1]
    x = t
    y = s
    plt.plot(x,y)
    plt.xlabel('time')
    plt.ylabel('distance')
    plt.title('s-t')
    plt.show()

caculate()



