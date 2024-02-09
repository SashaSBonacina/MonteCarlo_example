import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

n = 1000000
samples = 0
successful_samples = 0
new_baby = ''
x = []
y = []
for i in range(n):
    num_girls = 3
    num_boys = 2
    if (random.randint(0, 1)) == 1:
        new_baby = 'b'
        num_boys += 1
    else:
        new_baby = 'g'
        num_girls += 1
    if 'b' == np.random.choice(['b','g'], p=[num_boys/6, num_girls/6]):
        samples += 1
        if new_baby == 'b':
            successful_samples += 1
    if i % (n/100) == 0:        
        if samples != 0:
            x.append(successful_samples/samples)
            y.append(i)  
            
distances = np.abs(np.array(x) - 0.6)
normalized_distances = distances / np.max(distances)
colors = cm.viridis(normalized_distances)

for i in range(len(x)):
        plt.xlim(0.4, 0.8)
        plt.ylim(0,n)
        plt.title("Monte Carlo Simulation")
        plt.xlabel("Recorded Value")
        plt.ylabel("Iteration")
        plt.annotate(round(x[i],5), xy=(x[i], y[i]), xytext=(0.45, n/2),
             fontsize=12, color='white', backgroundcolor=colors[i])

        plt.axvline(x=0.6, color='red', linestyle='--', linewidth=1)
        plt.scatter(x[i], y[i], c=colors[i], alpha=0.5)
        plt.pause(0.001)

plt.show() 
            
