import matplotlib.pyplot as plt
import math 
k=15
dx=0.001
x0=0.
x=[]
s=[]
x.append(x0)
s.append(0)
x_1=1
a1=range(k)
f1=[]
for j in range(k):
    for i in range(int((x_1-x0)/dx)):
        x.append((4*(a1[j]+1)**0.5*(x_1**(a1[j]+1)-(x0+i*dx)**(a1[j]+1))**-0.5*dx))
        s.append(s[-1]+x[-1])
    f1.append(s[-1])
   # print s[-1]
del x[:]
del s[:]
x.append(x0)
s.append(0)
x_1=2
a2=range(k)
f2=[]
for j in range(k):
    for i in range(int((x_1-x0)/dx)):
        x.append((4*(a2[j]+1)**0.5*(x_1**(a2[j]+1)-(x0+i*dx)**(a2[j]+1))**-0.5*dx))
        s.append(s[-1]+x[-1])
    f2.append(s[-1])
   # print s[-1]
del x[:]
del s[:]
x.append(x0)
s.append(0)
x_1=3
a3=range(k)
f3=[]
for j in range(k):
    for i in range(int((x_1-x0)/dx)):
        x.append((4*(a3[j]+1)**0.5*(x_1**(a3[j]+1)-(x0+i*dx)**(a3[j]+1))**-0.5*dx))
        s.append(s[-1]+x[-1])
    f3.append(s[-1])
   # print s[-1]
del x[:]
del s[:]
x.append(x0)
s.append(0)
x_1=4
a4=range(k)
f4=[]
for j in range(k):
    for i in range(int((x_1-x0)/dx)):
        x.append((4*(a4[j]+1)**0.5*(x_1**(a4[j]+1)-(x0+i*dx)**(a4[j]+1))**-0.5*dx))
        s.append(s[-1]+x[-1])
    f4.append(s[-1])
   # print s[-1]
del x[:]
del s[:]
x.append(x0)
s.append(0)
x_1=5
a5=range(k)
f5=[]
for j in range(k):
    for i in range(int((x_1-x0)/dx)):
        x.append((4*(a5[j]+1)**0.5*(x_1**(a5[j]+1)-(x0+i*dx)**(a5[j]+1))**-0.5*dx))
        s.append(s[-1]+x[-1])
    f5.append(s[-1])
   # print s[-1]
#The following codes plot the data.
plt.figure(1)
line_1,=plt.plot(a1,f1)
line_2,=plt.plot(a2,f2)
line_3,=plt.plot(a3,f3)
line_4,=plt.plot(a4,f4)
line_5,=plt.plot(a5,f5)
plt.ylabel('period')
plt.xlabel('index.a')
plt.title('the different period for different a')
plt.legend([line_1,line_2,line_3,line_4,line_5],['amplitude=1','amplitude=2','amplitude=3','amplitude=4','amplitude=5',],fontsize='x-small')
plt.show()