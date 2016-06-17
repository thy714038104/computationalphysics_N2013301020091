# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:29:51 2016

@author: thy
"""

import matplotlib.pyplot as plt
import numpy as np
import math
theta0=0.2
theta1=0.2001
omg0=0.0
t0=0.0
l=9.8
g=9.8
dt=0.04
time=400.0
OMG_D=2.0/3
theta=[theta0]
theta1=[theta1]
omg1=[omg0]
omg=[omg0]
t1=[t0]
t=[t0]
t2=[t0]
n=int(time/dt)
OMG_D=OMG_D
F_D=[0.0,1.5,1.2]
I=range(n)
q=[0,1.5,0.5]
delta=[]
for i in I:
    omg.append(omg[i]+(-g/l*math.sin(theta[i])-q[2]*omg[i]+F_D[2]*math.sin(OMG_D*t[i]))*dt)
    theta.append(theta[i]+omg[i+1]*dt)
    if theta[i+1]<-math.pi:
       theta[i+1]=theta[i+1]+2*math.pi
    if theta[i+1]>math.pi:
       theta[i+1]=theta[i+1]-2*math.pi
    t.append(t[i]+dt)
for i in I:
    omg1.append(omg1[i]+(-g/l*math.sin(theta1[i])-q[2]*omg1[i]+F_D[2]*math.sin(OMG_D*t1[i]))*dt)
    theta1.append(theta1[i]+omg1[i+1]*dt)
    if theta1[i+1]<-math.pi:
       theta1[i+1]=theta1[i+1]+2*math.pi
    if theta1[i+1]>math.pi:
       theta1[i+1]=theta1[i+1]-2*math.pi
    t1.append(t1[i]+dt)
for i in I:
    l=theta1[i]-theta[i]
    #delta.append(l)
    if l>=0:
       l=l
       delta.append(l)
    if l<0:
       l=-l
    delta.append(l)
    t2.append(t2[i]+dt)
delta=delta[1:int(10000.00000)]
t1=t1[1:int(10000.00000)]
# EULER CROMER METHOD are used
plt.plot(t1, delta, '--',label='F_D=0.5')
plt.title(u'Nonlinear Pendulum - delta Angle',fontsize=14)
plt.xlabel(u'time(s)',fontsize=14)
plt.ylabel(u'delta angel (rad)',fontsize=14)
plt.legend(fontsize=12,loc='best')
plt.show()
