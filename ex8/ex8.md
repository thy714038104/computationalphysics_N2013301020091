# EX8 
##摘要
本程序主要分析了非简谐振动的周期与非简谐力之间的的具体关系，主有Euler methond,Euler-cromer methond,Runge-Kutta methond，本文主要采用Euler-cromer methond,并对不同的计算方法进行对比。
##正文
###周期的解析式
非简谐运动的运动微分方程:  
![](http://latex.codecogs.com/gif.latex?dx^2/d^2t=-kx^a)  
运动过程中最大的位移:  
![](http://latex.codecogs.com/gif.latex?x_m)  
上式的解析式即运动解为:    
![](http://latex.codecogs.com/gif.latex?T%3D4%5Csqrt%7B%5Cfrac%7Ba&plus;1%7D%7Bk%7D%7D%5Cint_%7B0%7D%5E%7Bx_m%7D%28%28x_m%29%5E%7Ba&plus;1%7D-%28x%5E%7Ba&plus;1%7D%29%29%5E%7B-1/2%7Ddx)  
当a=1时，![](http://latex.codecogs.com/gif.latex?T%3D2%5Cpi%20%5Csqrt%7B%28a&plus;1%29/k%7D);  
若a不为1时，周期T与![](http://latex.codecogs.com/gif.latex?x_m)最大位移相关。  

###不同计算方法的比较
我们以二阶常微分方程为例  
![](http://latex.codecogs.com/gif.latex?dx^2/d^2t=-x)  
![](http://latex.codecogs.com/gif.latex?x(0)=1)  
![](http://latex.codecogs.com/gif.latex?x'(0)=1)  
可以得到解析解为  
![](http://latex.codecogs.com/gif.latex?x(t)=cos(t))  
接下来利用Euler methond，Euler-cromer methond,Runge-Kutta方法分别计算  
[程序](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex8/1.py)  
![计算结果对比图](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex8/1.png)  

###非简谐运动
![](http://latex.codecogs.com/gif.latex?dx^2/d^2t=-kx^a)  
利用四阶R—K算法计算其数值解，在k = 1 , a = 1,2,3,4时的计算结果  
[程序](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex8/5.py)  
![计算结果对比图](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex8/2.png)  
从图中可以看出，当a=1，3时，运动稳定，当a=2，4时，在4s后运动变得不稳定，且离开平衡位置越来越大，可从角度的变化可以看出。  
上式运动的周期表达式为  
![](http://latex.codecogs.com/gif.latex?T%3D4%5Csqrt%7B%5Cfrac%7Ba&plus;1%7D%7Bk%7D%7D%5Cint_%7B0%7D%5E%7Bx_m%7D%28%28x_m%29%5E%7Ba&plus;1%7D-%28x%5E%7Ba&plus;1%7D%29%29%5E%7B-1/2%7Ddx)  
当a=1时，![](http://latex.codecogs.com/gif.latex?T%3D2%5Cpi%20%5Csqrt%7B%28a&plus;1%29/k%7D)   
在上面的结果中给出  
![](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex8/3.png)  
上图显示了在k=1时，不同的a的值对应不同的周期，其中当a=1时，周期大致呈线性关系。
##致谢
感谢刘星辰和陈洋遥同学
