import os
import glob
import numpy as np
import errno
import math


class dataValues:
	def __init__(self):
		self.frame = '1'
		self.Z = [] 


def slope(v1, v2):
	angle = np.arctan2((v2[1] - v1[1]) , (v2[0] - v1[0]))

	if angle < 0:
		angle = angle + (2 * np.pi)
	return angle


def main():
	for instance in range(2):
		curPath = os.getcwd() 
		if instance: 
			filePath = os.path.join(curPath,'hod_d1.t')
			if os.path.isfile(filePath): 
				os.remove(filePath)
			dataPath = os.path.join(curPath,'dataset/test/*.txt')
		else: 
			filePath = os.path.join(curPath,'hod_d1')
			if os.path.isfile(filePath):
				os.remove(filePath)
			dataPath = os.path.join(curPath,'dataset/train/*.txt')
		files = glob.glob(dataPath) 
		for name in files:
			
			dataPoints = [] 
			dataPoints.append(dataValues()) 
			count = 0
			with open(name,'r') as f, open(filePath,'a+') as d:
				content = f.readlines()
				for data in content:
					info = data.split()
					if info[0] != dataPoints[count].frame:
						dataPoints.append(dataValues())
						count = count + 1
						dataPoints[count].frame = info[0]
					if math.isnan(float(info[3])):
						dataPoints[count].Z.append([[0.0,0.0],[0.0,0.0],[0.0,0.0]])
					else:
						dataPoints[count].Z.append([[float(info[2]),float(info[3])],[float(info[3]),float(info[4])],[float(info[4]),float(info[2])]])
				
				noOfFrames = len(dataPoints)
				vecLength = len(dataPoints[0].Z) 
				binArray = list(range(0,361,45)) 
				binArray = [((x*np.pi)/180) for x in binArray] 
				for i in range(vecLength): 
					for plane in range(3): 
						
						plotVec = [slope(dataPoints[c].Z[i][plane],dataPoints[c+1].Z[i][plane]) for c in range(0,noOfFrames-1,1)]
						histData,binData = np.histogram(plotVec,bins=binArray)
						histData = [x/noOfFrames for x in histData] 
						

						featureVec = [[val,binData[c],binData[c+1]] for c,val in enumerate(histData)] 
						writeVal = ''.join(str(e) for e in featureVec) 
						d.write(writeVal)

						plotVecHalf = [plotVec[:len(plotVec)//2],plotVec[len(plotVec)//2:]]
						histData,binData = np.histogram(plotVecHalf[0],bins=binArray)
						histData = [x/noOfFrames for x in histData] 
							
						featureVec = [[val,binData[c],binData[c+1]] for c,val in enumerate(histData)] 
						writeVal = ''.join(str(e) for e in featureVec) 
						d.write(writeVal)
							
						histData,binData = np.histogram(plotVecHalf[1],bins=binArray)
						histData = [x/noOfFrames for x in histData] 
							

						featureVec = [[val,binData[c],binData[c+1]] for c,val in enumerate(histData)] 
						writeVal = ''.join(str(e) for e in featureVec)
						d.write(writeVal)
							

						plotVecQuarter = [plotVecHalf[0][:len(plotVecHalf[0])//2],plotVecHalf[0][len(plotVecHalf[0])//2:],plotVecHalf[1][:len(plotVecHalf[1])//2],plotVecHalf[0][len(plotVecHalf[0])//2:]]
						histData,binData = np.histogram(plotVecQuarter[0],bins=binArray)
						histData = [x/noOfFrames for x in histData] 
							

						featureVec = [[val,binData[c],binData[c+1]] for c,val in enumerate(histData)] 
						writeVal = ''.join(str(e) for e in featureVec) 
						d.write(writeVal)
							

						histData,binData = np.histogram(plotVecQuarter[1],bins=binArray)
						histData = [x/noOfFrames for x in histData] 

							

						featureVec = [[val,binData[c],binData[c+1]] for c,val in enumerate(histData)] 
						writeVal = ''.join(str(e) for e in featureVec) 
						d.write(writeVal)
							

						histData,binData = np.histogram(plotVecQuarter[2],bins=binArray)
						histData = [x/noOfFrames for x in histData] 
							

						featureVec = [[val,binData[c],binData[c+1]] for c,val in enumerate(histData)] 
						writeVal = ''.join(str(e) for e in featureVec) 
						d.write(writeVal)
							
						histData,binData = np.histogram(plotVecQuarter[3],bins=binArray)
						histData = [x/noOfFrames for x in histData] 
							

						featureVec = [[val,binData[c],binData[c+1]] for c,val in enumerate(histData)] 
						writeVal = ''.join(str(e) for e in featureVec) 

						d.write(writeVal)
				d.write('\n')
			
if __name__=="__main__":
	main()
