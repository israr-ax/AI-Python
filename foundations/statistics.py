import matplotlib.pyplot as plt
import numpy as np 
'''
Generate 100 random normal values
Calculate:
Mean,Standard deviation
Plot histogram
Check if shape looks normal
'''
np.random.seed(42)
num=np.random.normal(loc=0, scale=1, size=1000)

mean=np.mean(num)
std_dev=np.std(num)
print(f"Mean:{mean: .4f} \nStandard deviation: {std_dev: .4f}" )

plt.subplot(1,2,1)
plt.hist(num, bins=30, color='blue', edgecolor='black')
plt.title("Normal Distribution Histogram")
plt.xlabel('Values')
plt.ylabel('Frequency')




# Check Shape 

Skewed_data= np.random.exponential(scale=1, size=100)
print(f"Mean:{np.mean(Skewed_data): .4f} \nStandard deviation: {np.std(Skewed_data): .4f}" )
from scipy.stats import skew

print("Normal skew:", skew(num))
print("Exponential skew:", skew(Skewed_data))

# Plot Skewed Histogram
plt.subplot(1,2,2) 
plt.hist(Skewed_data, bins=30, color='orange', edgecolor='black')
plt.title("Right Skewed  Distribution Histogram")
plt.xlabel('Values')
plt.ylabel('Frequency')


plt.suptitle('Right-Skewed And Normal Distribution')
plt.tight_layout()
plt.show()

