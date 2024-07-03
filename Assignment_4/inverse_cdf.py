import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
import matplotlib.animation as ani
from scipy.special import erfinv
import scipy.stats
import math

x=[]

def inverse_normal_cdf(u, mean, variance):
	std_dev = math.sqrt(variance)
	return mean + std_dev * math.sqrt(2) * erfinv(2*u - 1)

def create_dataset(mean, variance, a, b):
	n_samples=100000
	for i in range(n_samples):
		u = np.random.uniform(0, 1)
		while( u < a or u > b):
			u = np.random.uniform(0, 1)
		x.append(inverse_normal_cdf(u, mean, variance))



mean = float(input("Enter mean of the normal distribution : "))
variance = float(input("Enter variance of the normal distribution : "))
a = float(input("Enter Value of a between 0 and 1 : "))
while(a < 0 or a > 1):
	a = float(input("Enter Value of a between 0 and 1 : "))
b = float(input("Enter Value of b between 0 and 1 : "))
while(b > 1 or b < 0 or b < a):
	b = float(input("Enter Value of b between 0 and 1 : "))
create_dataset(mean, variance, a,b)

fig, ax = plt.subplots()
y = np.linspace(inverse_normal_cdf(a,mean,variance), inverse_normal_cdf(b,mean,variance), 101)
ax.plot(y, scipy.stats.norm.pdf(y, mean, np.sqrt(variance)), color='r')
ax.hist(x, bins=500, density=True, alpha=0.6, color='b')
ax.set_title('Histogram of normal distribution with mean='+str(mean)+' and variance='+str(variance) + f"\n for uniform samples over a = {a} and b = {b}")
ax.set_ylabel('Frequency')
ax.set_xlabel('Value')
plt.show()

