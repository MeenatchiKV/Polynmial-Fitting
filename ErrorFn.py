import scipy as sp
import matplotlib.pyplot as plt

def error(f,x,y):
    return sp.sum((f(x)-y)**2)


data = sp.genfromtxt("E:\\MLPY\\book1\\ch01\\data\\web_traffic.tsv",delimiter="\t")
x=data[:,0]
y=data[:,1]
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]



fp1 = sp.polyfit(x,y,1)
f1 = sp.poly1d(fp1)

fp2 = sp.polyfit(x,y,2)
f2 = sp.poly1d(fp2)

fp3 = sp.polyfit(x,y,3)
f3 = sp.poly1d(fp3)

fp10 = sp.polyfit(x,y,10)
f10 = sp.poly1d(fp10)

fp100 = sp.polyfit(x,y,100)
f100 = sp.poly1d(fp100)

print("error %s"%error(f1,x,y))
print("error %s"%error(f2,x,y))
print("error %s"%error(f3,x,y))
print("error %s"%error(f10,x,y))
print("error %s"%error(f100,x,y))


