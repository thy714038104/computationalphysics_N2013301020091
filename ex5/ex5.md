# EX5
##摘要
　　实际过程中物体下落过程会受到空气阻力的影响，则速度与时间的关系不是绝对的线性关系，参照习题1.3，本文进一步运用Euler法对较复杂的常微分方程进行求解，并优化作图细节。
##正文
###问题分析
　　我们考虑一个简单的例子，即阻力只依赖于速度。假设物体的速度方程如下：  
![](http://latex.codecogs.com/gif.latex?dv/dt=g-bv)
这里b为常数，来自于阻力，注意到阻力是负的（假设b>0）,而且其随着速度同数量级增长。  
对公式进行Euler展开有：  
![](http://latex.codecogs.com/gif.latex?v%28t&plus;%5CDelta%20t%29%3Dv%28t%29&plus;%28a-bv%28t%29%29dt)
这就是待计算的迭代方程。
###代码程序设计
　　由分析所得，运用Euler法，程序语言为:  
　　![](http://latex.codecogs.com/gif.latex?v%28i&plus;1%29%3Dv%28i%29&plus;%28a-bv%28i%29%29t)

　　由此写出[程序](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex5/ex5.py)。
###程序实现
　　运行程序,可得如下图示结果：  
![](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex5/1.png)
　　该图反映了初速度为0和30m/s两种情况下的速度与时间关系。
##结论
　　在此模型中，由程序结论图可以看出：
速度小于最终速度时，速度将不断增大，随着速度的增大加速度不断减小，直至最终阻力与重力平衡，达至最终速度。
速度大于最终速度时，速度将不断减小，随着速度的减小加速度不断减小，直至最终阻力与重力平衡，达至最终速度
。
当然，这些结论都基于下落距离足够大。
##致谢
　　感谢陈一恒同学

