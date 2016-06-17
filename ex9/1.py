# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:28:52 2016

@author: thy
"""

import matplotlib.pyplot as plt
import numpy as np
import math
# class CROMER
class CROMER_1(object):
    def __init__(self, _theta0=0.2, _omg0=0.0, _t0=0.0, _l=9.8,_g=9.8, _dt=0.04, _time=60.0,_q=0.5,_OMG_D=2.0/3):
        self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
        self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
        self.OMG_D=_OMG_D
        self.F_D=[0.0,0.5,1.0]
        self.I=range(self.n)
        self.q=[0.0,0.5,1.0]
    def calculate(self):
        for i in self.I:
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q[0]*self.omg[i]+self.F_D[1]*math.sin(self.OMG_D*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label='F_D=0')
    def plot_w(self,_ax):
        _ax.plot(self.t,self.omg,'--',label='F_D=0')
class CROMER_2(CROMER_1):
    def calculate(self):
        for i in self.I:
            self.omg.append(self.omg[i]+(-self.g/self.l*math.sin(self.theta[i])-self.q[1]*self.omg[i]+self.F_D[1]*math.sin(self.OMG_D*self.t[i]))*self.dt)
            self.theta.append(self.theta[i]+self.omg[i+1]*self.dt)
            if self.theta[i+1]<-math.pi:
               self.theta[i+1]=self.theta[i+1]+2*math.pi
            if self.theta[i+1]>math.pi:
               self.theta[i+1]=self.theta[i+1]-2*math.pi
            self.t.append(self.t[i]+self.dt)
    def plot_theta(self,_ax):
        _ax.plot(self.t, self.theta, '--',label='F_D=0.5')
    def plot_w(self,_ax):
        _ax.plot(self.t,self.omg,'--',label='F_D=0.5')
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
        _ax.plot(self.t, self.theta, '--',label='F_D=1.0')
    def plot_w(self,_ax):
        _ax.plot(self.t,self.omg,'--',label='F_D=1.0')
# plot :
# EULER CROMER METHOD are used
fig= plt.figure(figsize=(14,7))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
comp= CROMER_1()
comp.calculate()
comp.plot_theta(ax1)
comp.plot_w(ax2)
comp=CROMER_2()
comp.calculate()
comp.plot_theta(ax1)
comp.plot_w(ax2)
comp=CROMER_3()
comp.calculate()
comp.plot_theta(ax1)
comp.plot_w(ax2)
ax1.set_title('Nonlinear Pendulum - Angle',fontsize=14)
ax2.set_title('Nonlinear Pendulum - W',fontsize=14)
ax1.set_xlabel('time(s)',fontsize=14)
ax1.set_ylabel('Angel (rad)',fontsize=14)
ax2.set_xlabel('time(s)',fontsize=14)
ax2.set_ylabel('w(rad/s)',fontsize=14)
ax1.legend(fontsize=12,loc='best')
ax2.legend(fontsize=12,loc='best')
plt.show(fig)