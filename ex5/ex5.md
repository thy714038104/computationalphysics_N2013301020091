# Homework5

炮弹运动轨迹；考虑阻力


##**摘要：**
炮弹在未受空气阻力，并且不考虑科里奥利力以及其他因素时，将会按照抛物线进行运动。再次我们将把空气阻力的作用考虑进来并认为空气密度不随高度而变化，即  
![](http://latex.codecogs.com/gif.latex?f=kv)  
中，参数k为常数对炮弹的运动轨迹进行计算，并在二维平面上展示炮弹的运动轨迹。这里将炮弹简化为了一个质点，考虑重力与空气阻力下的运动。
##**分析：**
1、不考虑空气阻力的情况下，炮弹的动力学方程为：  
![](http://latex.codecogs.com/gif.latex?d^2x/dt^2=0)  
![](http://latex.codecogs.com/gif.latex?d^2y/dt^2=-g)  
2、考虑空气阻力的情况下，炮弹的动力学方程变为：  
![](http://latex.codecogs.com/gif.latex?d^2x/dt^2=-f_x/m)  
![](http://latex.codecogs.com/gif.latex?d^2y/dt^2=-g-f_y/m)  
其中，空气阻力与速度成正比，即：
![](http://latex.codecogs.com/gif.latex?f_x=-kv_x)
![](http://latex.codecogs.com/gif.latex?f_y=-kv_y)
同样可以用欧拉法来解决，因为是二阶微分方程，我们可以把二阶微分方程分解为两个一阶微分方程，参考书上给出的方程，进行在五空气阻力和有空气阻力时依据角度的不同进行对比。

![程序](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex5/bullet.py)
##图像
![27](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex5/27.png)  
![45](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex5/27.png)
![63](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex5/63.png)
##结论：
从图中可以看出在无空气阻力时，当发射角为45°是射程最远，存在空气阻力的情况下，炮弹射程与不存在空气阻力相差很多。在对称的发射角下，角度越小，受到空气阻力的影响越小。
##致谢
感谢张爽同学提供的程序
