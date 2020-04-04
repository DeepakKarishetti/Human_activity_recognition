import glob
import math
import numpy as np
import os
import sys

a = sys.argv[1]

def get_distance(a, b):
    distance = (np.sum(np.square((np.array(a) - np.array(b))))) 
    return distance

class dataValues:
    def __init__(self):
        self.frameID = '1'
        self.xyz = []


def slope(a,b):
    angle = np.arctan2((b[1]-a[1]),(b[0]-a[0]))
    distance = get_distance(a,b)
    return angle * distance

def main():
    curPath = os.getcwd() 
    if int(a) == 1:    
        dataPath = os.path.join(curPath,'dataset/train/*.txt')
    else:
        dataPath = os.path.join(curPath, 'dataset/test/*.txt')
    
    files = glob.glob(dataPath) 
    files = sorted(files)

    for file_number, name in enumerate(files):

        file_name = os.path.split(name) 

        dataPoints = [] 
        dataPoints.append(dataValues()) 
        count = 0

        with open(name,'r') as f:
            content = f.readlines()
            for data in content:
                info = data.split()
                if info[0] != dataPoints[count].frameID:
                    dataPoints.append(dataValues())
                    count = count + 1
                    dataPoints[count].frameID = info[0]
                if math.isnan(float(info[3])):
                    dataPoints[count].xyz.append([[0.0,0.0],[0.0,0.0],[0.0,0.0]])
                else:
                    dataPoints[count].xyz.append([[float(info[2]),float(info[3])],[float(info[3]),float(info[4])],[float(info[4]),float(info[2])]])

            
            concatenate_list = list()
            
            frame = len(dataPoints)
            l = len(dataPoints[0].xyz) 
            binArray = list(range(0,361,45)) 
            binArray = [((x*np.pi)/180) for x in binArray] 
            for i in range(l): 
                for plane in range(3):                  
                    p_vec = [slope(dataPoints[c].xyz[i][plane], dataPoints[c+1].xyz[i][plane]) for c in range(0, frame-1,1)]
                    hist, bid = np.histogram(p_vec, bins=binArray)
                    
                    for x in hist:
                        concatenate_list.append(x / frame)
                   

                    p_half = [p_vec[:len(p_vec)//2],p_vec[len(p_vec)//2:]]
                    hist, bid = np.histogram(p_half[0], bins=binArray)
                    
                    for x in hist:
                        concatenate_list.append(x / frame)
                    
                    hist,bid = np.histogram(p_half[1], bins=binArray)
                    for x in hist:
                        concatenate_list.append(x / frame)
                    

                    p_quat = [p_half[0][:len(p_half[0])//2], p_half[0][len(p_half[0])//2:], p_half[1][:len(p_half[1])//2],  p_half[0][len(p_half[0])//2:]]
                    hist, bid = np.histogram(p_quat[0], bins=binArray)
                    for x in hist:
                        concatenate_list.append(x / frame)
                    

                    hist, bid = np.histogram(p_quat[1], bins=binArray)
                    for x in hist:
                        concatenate_list.append(x / frame)
                    
                    hist, bid = np.histogram(p_quat[2], bins=binArray)
                    for x in hist:
                        concatenate_list.append(x / frame)
                    

                    hist, bid = np.histogram(p_quat[3], bins=binArray)
                    for x in hist:
                        concatenate_list.append(x / frame)

                    
            concatenate_list = ['{}:{}'.format(k+1, str(i)) for k, i in enumerate(concatenate_list)]
            
            if int(a) == 1:
                
                with open('hod_d1_formated', 'a+') as f:

                    if(str(file_name[1][1:3]) == '08'):
                        n1 = ("8 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n1))

                    if(str(file_name[1][1:3]) == '10'):
                        n2 = ("10 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n2))           

                    if(str(file_name[1][1:3]) == '12'):
                        n3 = ("12 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n3))

                    if(str(file_name[1][1:3]) == '13'):
                        n4 = ("13 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n4))

                    if(str(file_name[1][1:3]) == '15'):
                        n5 = ("15 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n5))

                    if(str(file_name[1][1:3]) == '16'):
                        n6 = ("16 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n6))
            else:
                with open('hod_d1_formated.t', 'a+') as f:

                    if(str(file_name[1][1:3]) == '08'):
                        n1 = ("8 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n1))

                    if(str(file_name[1][1:3]) == '10'):
                        n2 = ("10 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n2))           

                    if(str(file_name[1][1:3]) == '12'):
                        n3 = ("12 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n3))

                    if(str(file_name[1][1:3]) == '13'):
                        n4 = ("13 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n4))

                    if(str(file_name[1][1:3]) == '15'):
                        n5 = ("15 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n5))

                    if(str(file_name[1][1:3]) == '16'):
                        n6 = ("16 {}".format(' '.join(concatenate_list)))
                        f.write('{}\n'.format(n6))
                    
if __name__=="__main__":
    main()
