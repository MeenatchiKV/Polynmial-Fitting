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

fa = sp.poly1d(sp.polyfit(xa,ya,1))
fb = sp.poly1d(sp.polyfit(xb,yb,1))
'''
plt.scatter(x,y)
plt.title("Web Traffic")
plt.xlabel("Time")
plt.ylabel("hits/hr")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()'''


fp1a = sp.polyfit(xa,ya,1)
f1a = sp.poly1d(fp1a)

fp2a = sp.polyfit(xa,ya,2)
f2a = sp.poly1d(fp2a)

fp3a = sp.polyfit(xa,ya,3)
f3a = sp.poly1d(fp3a)

fp1b = sp.polyfit(xb,yb,1)
f1b = sp.poly1d(fp1b)

fp2b = sp.polyfit(xb,yb,2)
f2b = sp.poly1d(fp2b)

fp3b = sp.polyfit(xb,yb,3)
f3b = sp.poly1d(fp3b)

fae1 = error(f1a,xa,ya)
fae2 = error(f2a,xa,ya)
fae3 = error(f3a,xa,ya)

fbe1 = error(f1b,xb,yb)
fbe2 = error(f2b,xb,yb)
fbe3 = error(f3b,xb,yb)

print("Total Error")
print("Error 1: %s"%(fae1+fbe1))
print("Error 2: %s"%(fae2+fbe2))
print("Error 3: %s"%(fae3+fbe3))

print("Error for 2nd Phase")
print("Error 1: %s",fbe1)
print("Error 2: %s",fbe2)
print("Error 3: %s",fbe3)
