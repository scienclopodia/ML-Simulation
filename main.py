# A piece of code that is supposed to do some ML algs.
# Made by Rayner Setiawan

from cost import costCalculation

def main():
    # dataPointLocation = [(1, 1), (2, 2), (3, 3), (4, 4)]
    dataPointLocation = [(1, 1)]
    
    dataPointLocationX = []
    dataPointLocationY = []

    for i in range(len(dataPointLocation)):
        dataPointLocationX.append(dataPointLocation[i][0])
        dataPointLocationY.append(dataPointLocation[i][1])

    # Actual cost calculation section.

    intercept = 0

    slope = 0

    costCalc = costCalculation(dataPointLocationX, dataPointLocationY, intercept, slope)
    
    print(costCalc.calculateCost())

if __name__ == "__main__":
	main()
    
