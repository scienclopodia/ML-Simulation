import matplotlib.pyplot as plt
import numpy as np
from cost import costCalculation

x = np.linspace(-5, 5, 200)

costPlotY = []
costPlotX = []

for i in range(1, 10):
    cost = costCalculation(x, np.square(x), 0, i)
    
    costPlotY.append(cost.calculateCost())
    costPlotX.append(i)

plt.subplot(1, 2, 1)
plt.plot(x, np.square(x))

plt.subplot(1, 2, 2)
plt.plot(costPlotX, costPlotY)

plt.show()
