import scipy as sp
import matplotlib.pyplot as plt

def error(f,x,y):
    return sp.sum((f(x)-y)**2)


data = sp.genfromtxt("E:\\MLPY\\book1\\ch01\\data\\web_traffic.tsv",delimiter="\t")
inflection = 3.5*7*24 #inflection point
inflection=int(inflection)

print(inflection)

x=data[:,0]
y=data[:,1]
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]


xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]

fp3b = sp.polyfit(xb,yb,3)
f3b = sp.poly1d(fp3b)

fbe3 = error(f3b,xb,yb)

print("Error 3: %s",fbe3)

print(f3b)

print(f3b-100000)

from scipy.optimize import fsolve
reached_max = fsolve(f3b-100000, 800)/(7*24)
print("100000 hits/hr expected at week %s" % reached_max[0])
