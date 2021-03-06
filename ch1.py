import scipy as sp
import matplotlib.pyplot as plt

def error(f,x,y):
    return sp.sum((f(x)-y)**2)


data = sp.genfromtxt("E:\\MLPY\\book1\\ch01\\data\\web_traffic.tsv",delimiter="\t")
x=data[:,0]
y=data[:,1]
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]

plt.scatter(x,y)
plt.title("Web Traffic")
plt.xlabel("Time")
plt.ylabel("hits/hr")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()


fp1 = sp.polyfit(x,y,1)
f1 = sp.poly1d(fp1)

fp2 = sp.polyfit(x,y,2)
f2 = sp.poly1d(fp2)

fp3 = sp.polyfit(x,y,3)
f3 = sp.poly1d(fp3)
#print("model param %s" %fp1)
#print("res %s" %res)

print("error %s"%error(f1,x,y))
print("error %s"%error(f2,x,y))
print("error %s"%error(f3,x,y))

fx=sp.linspace(0,x[-1],1000)
plt.plot(fx,f1(fx),linewidth=4)
plt.plot(fx,f2(fx),linewidth=4)
plt.plot(fx,f3(fx),linewidth=4)

plt.show()



