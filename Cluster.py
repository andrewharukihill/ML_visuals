#Cluster.py
#Visualization of K-Means Clustering Algorithm
#Andrew Hill

#Import modules
import random
import numpy
import math
import matplotlib.pyplot as plt


def generateData(numPoints,x,y):
	"""Generates two datasets that are normally distributed around different means"""
	for i in range(0,numPoints):
		if (i % 2 == 0):
			x.append(random.normalvariate(25, 15))
			y.append(random.normalvariate(25, 15))
			 
			
		else:
			x.append(random.normalvariate(75, 15))
			y.append(random.normalvariate(75, 15))

def calculateDist(kSet1, kSet2, x, y, group, iteration):
	"""Calculates distance from cluster mean to a point"""
	kSet1Dist = 0
	kSet2Dist = 0
	
	for j in range(len(x)):
		k1Dist = math.sqrt((x[j] - kSet1[0])**2 + (y[j] - kSet1[1])**2)
		k2Dist = math.sqrt((x[j] - kSet2[0])**2 + (y[j] - kSet2[1])**2)

		if(k1Dist < k2Dist):
			group[iteration].append(1)
			kSet1Dist += k1Dist
		else:
			group[iteration].append(2)
			kSet2Dist += k2Dist

	return group
	
def newCenter(x, y, group, iteration, lastKSet1, lastKSet2):
	"""Calculates the new K-Means center for a cluster"""
	sumOneX = 0
	sumOneY = 0
	sumTwoX = 0
	sumTwoY = 0
	numOne = 0
	numTwo = 0

	for i in range(len(group[iteration])):
		if (group[iteration][i] == 1):
			sumOneX += x[i]
			sumOneY += y[i]
			numOne += 1
		else:
			sumTwoX  += x[i]
			sumTwoY += y[i]
			numTwo += 1

	if(numOne == 0):
		kSet1 = lastKSet1
	if(numTwo == 0):
		kSet2 = lastKSet2
	else:
		kSet1 = [sumOneX/numOne, sumOneY/numOne]
		kSet2 = [sumTwoX/numTwo, sumTwoY/numTwo]

	return (kSet1, kSet2)

def main():
	print("")
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)
	
	#Create empty lists to fill with data
	x = []
	y = []

	group = [[]]
	iteration = 1
	
	#Generate x and y data
		#Specify number of points to generate
	numPoints = 1000
	generateData(numPoints ,x,y)	

	#Plot initial data
	ax1.scatter(x, y)
	plt.show();

	#Plot initial data for K-Means algorithm
	fig2 = plt.figure()
	ax2 = fig2.add_subplot(1,1,1)
	ax2.scatter(x,y)
	
	lastKSet1 = [0, 0]
	lastKSet2 = [0, 0]

	#Set initial cluster points
	newKSet1 = [51, 50]
	newKSet2 = [50, 51]
	
	#While the distance between the last iteration's center is less than 0.01 from the 
	#current iteration's center, continue with K-Means calculation
	while(math.sqrt((lastKSet1[0] - newKSet1[0])**2 + (lastKSet1[1] - newKSet1[1])**2) > 0.01 and math.sqrt((lastKSet2[0] - newKSet2[0])**2 + (lastKSet2[1] - newKSet2[1])**2) > 0.01):
		#Plot K-Means centers
		ax2.plot(newKSet1[0], newKSet1[1], marker = "o", markersize = 8, color = "red")
		ax2.plot(newKSet2[0], newKSet2[1], marker = "o", markersize = 8, color = "yellow")

		lastKSet1 = newKSet1
		lastKSet2 = newKSet2

		group.append([])

		#Calculate distance between points and centers
		group = calculateDist(newKSet1, newKSet2, x, y, group, iteration)

		#Calculate new center
		newKSet1, newKSet2 = newCenter(x, y, group, iteration, lastKSet1, lastKSet2)
		
		#Print output of iteration
		print("Iteration " + str(iteration) + ":")
		print("   Set 1: [" + str(round(newKSet1[0],2)) + ", " + str(round(newKSet1[1],2)) + "]")
		print("   Set 2: [" + str(round(newKSet2[0],2)) + ", " + str(round(newKSet2[1],2)) + "]")
		iteration += 1

	#Print output of final iteration
	print("\nNumber of Iterations: " + str(iteration))
	print("Final K-Means Centers:")
	print("   Set 1: (" + str(round(newKSet1[0],2)) + ", " + str(round(newKSet1[1],2)) + ")")
	print("   Set 2: (" + str(round(newKSet2[0],2)) + ", " + str(round(newKSet2[1],2)) + ")")
	
	yellow = 0
	red = 0

	for i in range(len(group[iteration-1])):
		if(group[iteration - 1][i] % 2 != 0):
			red += 1
		else:
			yellow += 1

	#Print percentage of data points in each cluster (should be 50% for each)
	print("\nPercentage of Data Points In Each Cluster:")
	print("   Set 1: " + str(round(red/numPoints*100,1)) + "%")
	print("   Set 2: " + str(round(yellow/numPoints*100,1)) + "%")
	plt.show()

main()
