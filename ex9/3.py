# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:30:59 2016

@author: thy
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import pylab as pl
# class CROMER
class CROMER_1(object):
    def __init__(self, _theta0=0.2, _omg0=0.0, _t0=0.0, _l=9.8,_g=9.8, _dt=6.0*math.pi/1000, _time=6000.0,_q=0.5,_OMG_D=2.0/3):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
        self.OMG_D=_OMG_D
        self.F_D=[0.0,0.5,1.2]
        self.I=range(self.n)
        self.q=[0.5,0.5,0.5]
        self.theta1=[]
        self.omg1=[]
        self.p=0
    def calculate(self):
        for i in self.I:
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q[0]*self.omg[i]+self.F_D[1]*math.sin(self.OMG_D*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
            self.p=i%1000
            if self.p==0:
               self.theta1.append(self.theta[-1])
               self.omg1.append(self.omg[-1])
        self.theta1=self.theta1[100:]
        self.omg1=self.omg1[100:]
    def plot_theta(self,_ax):
        _ax.axes.scatter(self.theta1, self.omg1, marker='x',color='m',label='F_D=0.5')
        print len(self.theta1)
   # def plot_w(self,_ax):
       # _ax.plot(self.t,self.omg,'--',label='q=0')
class CROMER_2(CROMER_1):
    def calculate(self):
        for i in self.I:
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q[1]*self.omg[i]+self.F_D[2]*math.sin(self.OMG_D*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
            if i%1000==0:
               self.theta1.append(self.theta[-1])
               self.omg1.append(self.omg[-1])
        self.theta1=self.theta1[100:]
        self.omg1=self.omg1[100:]
  # def plot_theta(self,_ax):
     #   _ax.plot(self.t, self.theta, '---',label='q=0.1')
    def plot_w(self,_ax):
        _ax.axes.scatter(self.theta1,self.omg1,marker='o',color='b',label='F_D=1.2')
class CROMER_3(CROMER_1):
    def calculate(self):
        for i in self.I:
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q[2]*self.omg[i]+self.F_D[1]*math.sin(self.OMG_D*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label='q=0.5')
    def plot_w(self,_ax):
        _ax.plot(self.t,self.omg,'--',label='q=0.5')
# plot :
# EULER CROMER METHOD are used
fig= plt.figure(figsize=(14,7))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
comp= CROMER_1()
comp.calculate()
comp.plot_theta(ax1)
#comp.plot_w(ax2)
comp=CROMER_2()
comp.calculate()
#comp.plot_theta(ax1)
comp.plot_w(ax2)
#comp=CROMER_3()
#comp.calculate()
#comp.plot_theta(ax1)
#comp.plot_w(ax2)
ax1.set_title('Poincare section - $2n\pi$',fontsize=14)
ax2.set_title('Poincare section - $2n\pi$',fontsize=14)
ax1.set_xlabel('theta(rad)',fontsize=14)
ax1.set_ylabel('Angel volocity (rad/s)',fontsize=14)
ax2.set_xlabel('theta(rad)',fontsize=14)
ax2.set_ylabel('Angel volocity(rad/s)',fontsize=14)
ax1.legend(fontsize=12,loc='best')
ax2.legend(fontsize=12,loc='best')
plt.show(fig)