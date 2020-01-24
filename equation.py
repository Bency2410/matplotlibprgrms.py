from matplotlib import pyplot as plt
import numpy as np
x=np.arange(1,11)
y=x//2
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.title("y=x/2 graph")
plt.show()