import sys
import math

class costCalculation:
    def __init__(self, dataSetX, dataSetY, intercept, slope):
        self.dataSetX = dataSetX
        self.dataSetY = dataSetY
        self.intercept = intercept
        self.slope = slope
        self.cost = 0

    def calculateCost(self):
        """
        This is the cost function:
        1/2*len(dataSetX) * sum(len(dataSetX, 0): (self.intercept + dataSetX[i]*slope) - dataSetY[i] ^ 2
        Look it up. It's WAAAY simpler
        """

        # First, check if there someone cheekily made dataSetX and dataSetY different sizes.
        if len(self.dataSetX) != len(self.dataSetY):
            print("\n\n\n\n\n DATASET LENGTHS ARE DIFFERENT.")
            sys.exit()
        else: 
            pass

        self.hypothesisY = [] # Empty list.
        
        for i in range(len(self.dataSetX)):
            self.hypothesisY.append(self.intercept + (self.dataSetX[i]*self.slope)) # Make values for the hypothesis at the data's X loc.
        
        for i in range(len(self.dataSetX)):
            self.tempCost = (self.hypothesisY[i] - self.dataSetY[i]) ** 2
            self.cost += self.tempCost

        # Do the 1/2m part here!

        self.cost = self.cost * (1 / (2*len(self.dataSetX)))

        return self.cost

