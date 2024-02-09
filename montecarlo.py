import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import time
random.seed(33)
np.random.seed(33)
n = 1000000
samples = 0
successful_samples = 0
new_baby = ''
x = []
y = []
graph_samples = []
graph_result = []
graph_time = []
st = time.time()
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
            
    if i == 9 or i == 99 or i ==999 or i == 9999 or i == 99999 or i == 999999:
                # get the end time
        et = time.time()

        # get the execution time
        elapsed_time = et - st
        print(f'samples: {i}, result: {np.abs(0.6 - (successful_samples/samples))}, time: {elapsed_time}')
        graph_result.append(np.abs(0.6 - (successful_samples/samples)))
        graph_samples.append(i)
        graph_time.append(elapsed_time)
        
        
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
            


# Create figure and axes
fig, ax1 = plt.subplots()

# Plot data for graph_time on the left y-axis
color = 'tab:blue'
ax1.set_xlabel('Number of Samples')
ax1.set_ylabel('Time (seconds)', color=color)
ax1.plot(graph_samples, graph_time, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a secondary y-axis and plot data for graph_results
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Error', color=color)
ax2.plot(graph_samples, graph_result, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Set x-axis scale to log10 with specific tick marks
ax1.set_xscale('log')
ax1.set_xticks([10, 100, 1000, 10000, 100000, 1000000])

# Title
plt.title('How more samples affects MC Methods')

# Show plot
plt.show()
