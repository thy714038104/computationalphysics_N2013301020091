#EX9
##摘要
本次作业研究混沌(Chaos)现象。混沌是自然界普遍存在的现象。混沌过程的特点是：(1)混沌过程虽是在决定性系统进行的，然而系统的演化确是难以预测的，这主要是因为混沌系统对初值极为敏感。(2)混沌过程的不可预测性并不代表其完全无法研究，我们可以通过作出混沌过程相图的吸引子(attractor)来研究混沌过程，并对这个不可预测的过程给出一些“预测”。(3)另外，混沌过程的吸引子具有分形(fractal)结构，这本身就是混沌现象内禀的普遍规律。(4)周期倍增(periodic-doubling)是产生混沌的重要途径，周期倍增的Feigenbaum常数很好的体现了这种产生途径的普适性。本次作业的内容是： 主要讨论了有耗散和外加驱动力情况下单摆的运动情况，单摆会出现混沌现象，给出了在不同初始条件下的运动情况，了解混沌现象。
##正文
非线性摆呈现周期性运动，其轨迹与单摆大同小异，然而当把驱动、阻尼、非线性三个因素加在一起后，摆的运动方程可以写为:   
   ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%5Ctheta%20%7D%7Bdt%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%28%5Ctheta%29-q%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_Dsin%28%5COmega%20_Dt%29)  
其中右式第一项为重力的影响，第二项为耗散项，第三项为周期性驱动力，混沌现象主要由第三项体现出来。我们利用利用euler_cromer方法在 适当的初始条件下给出数值解。
[程序1](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex9/1.py)  
![](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex9/1.png)
其中左图显示了在不同的周期性驱动力作用下，转角随时间变化的图像。
右图显示了不同的周期性驱动力作用下，角速度随时间变化的关系图像。
显示了混沌摆在不同驱动力下转角和角速度的模拟图。  

 [程序2](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex9/2.py)  
 ![](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex9/2.png)
 其中左图显示了在不同大小的耗散力下，转角随时间变化的图像。
 右图显示了不同大小的耗散力下，角速度随时间变化的关系图像。
 从上面2幅图中可以看出，混沌与周期性驱动力的大小，耗散力都有关，当驱动力越大时，越容易出现混沌现象，耗散力越小时，也越容易出现混沌现象。  
![](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex9/5.png)  
![](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex9/6.png)
以上2图显示了在初始的角度相差0.001°的情形下，角速度随时间的变化，其中第一幅图的FD=1.2，第二幅为0.5。说明了在不同大小的驱动力下，周期性变化巨大。  

 [程序3](https://github.com/thy714038104/computationalphysics_N2013301020091/blob/master/ex9/3.py)  
  ![](https://raw.githubusercontent.com/thy714038104/computationalphysics_N2013301020091/master/ex9/4.png)
  
上图显示了在驱动力为0.5时没有出现混沌现象，为1.2时出现混沌现象。
##结论
混沌想象的出现与外加驱动力的周期，振幅都有关系，还与耗散大小相关，在初始值相差很小的情况下，经过一段时间会出现截然相反的情况。
##致谢
感谢让陈洋遥同学的帮助
