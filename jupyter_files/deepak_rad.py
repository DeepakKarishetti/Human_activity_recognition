import os
import glob
import numpy as np
from numpy import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

cur_path = os.getcwd()
file_path = 'dataset/train/'

#file_path = 'dataset/test/'

data_path = os.path.join(cur_path, file_path)
file_names = glob.glob(data_path+'*.txt')

bazooka = list()
for _file in file_names:
	with open(_file, 'r') as f:
		filename = f.readlines()
		bazooka.append(filename)
#print(bazooka)
'''
new_bazooka = list()
for i in range(len(bazooka)):
	x = [line[i].split(',') for line in bazooka]
	new_bazooka.append(x)
#print(new_bazooka)

joints_bazooka = list()
for i in new_bazooka:
	for k,elements in enumerate(i):
		if (k in [0,3,7,11,15,20]):
			joints_bazooka.append(elements)
#print(joints_bazooka)	'''
inter = list()
for small_list in bazooka:
	for line in small_list:
		line = line.replace('\n', '')
		#print(line)

		buffer_list = line.split()
		#print(buffer_list)
		inter.append(buffer_list)
		#print(inter)

		frame_id = buffer_list[0]
		joint_num = buffer_list[1]
		x = buffer_list[2]
		y = buffer_list[3]
		z = buffer_list[4]
#print(len(inter))
j1 = list()
j4 = list()
j8 = list()
j12 = list()
j16 = list()
j20 = list()
j_1 = '1'
j_4 = '4'
j_8 = '8'
j_12 = '12'
j_16 = '16'
j_20 = '20'
for i in inter:
	if i[1] == j_1:
		j1.append(i)
	elif i[1] == j_4:
		j4.append(i)
	elif i[1] == j_8:
		j8.append(i)
	elif i[1] == j_12:
		j12.append(i)
	elif i[1] == j_16:
		j16.append(i)
	elif i[1] == j_20:
		j20.append(i)
#m = len(j1)
#print((j1[m-1][4]))
#print((j4[m-1][0:5]))
#print((j8[m-1][0:5]))
#print((j12[m-1][0:5]))
#print((j16[m-1][0:5]))
#print((j20[m-1][0:5]))

'''
		if (this_frame == frame_id):
			if (joint_num in [3,7,11,15,19]:
				distance = get_distance()
				angle = get_angle()

d = list()		
def get_distance(d,j1,j2,j3,j4,j5,j6):
	for i in range(len(j1)-1):
		d_14 = pow(((j1[i][2]-j4[i][2] )**2 + (j1[i][3]-j4[i][3] )**2 + (j1[i][4]-j4[i][4] )**2), 0.5)
		print(d_14)		
#d.append(d_14)
'''
'''
		d[1] = pow(((j1[i][2]-j8[i][2] )**2 + (j1[i][3]-j8[i][3] )**2 + (j1[i][4]-j8[i][4] )**2), 0.5)
		d.append(d[1])
		d[2] = pow(((j1[i][2]-j12[i][2] )**2 + (j1[i][3]-j12[i][3] )**2 + (j1[i][4]-j12[i][4] )**2), 0.5)
		d.append(d[2])
		d[3] = pow(((j1[i][2]-j16[i][2] )**2 + (j1[i][3]-j16[i][3] )**2 + (j1[i][4]-j16[i][4] )**2), 0.5)
		d.append(d[3])
		d[4] = pow(((j1[i][2]-j20[i][2] )**2 + (j1[i][3]-j20[i][3] )**2 + (j1[i][4]-j20[i][4] )**2), 0.5)
		d.append(d[4])
'''
#print(d)
'''
def get_angle(x_c,y_c,z_c,x,y,z):
	m = x_c*x + y_c*y + z_c*z
	n = pow((x_c**2 + y_c*2 + z_c**2)*(x**2 + y**2 + z**2), 0.5)
	angle = acos(m/n) * 180 / math.pi
	return angle

def get_angle(d,j1,j4,j8,j12,j16,j20):
    m = (float(j1[i][2]))*(float(j4[i][2])) + (float(j1[i][3])*(float(j4[i][3])) + (float(j1[i][4])*(float(j4[i][4]))
    n = pow(((float(j1[i][2]))**2 + (float(j1[i][3]))**2 + (float(j1[i][4]))**2)*((float(j4[i][2]))**2 + (float(j4[i][3]))**2 + (float(j4[i][4]))**2), 0.5)
    angle = acos(m/n) * 180 / math.pi
    print(angle)
get_angle(d,j1,j4,j8,j12,j16,j20)

'''
'''
def get_angle(a,j1,j4,j8,j12,j16,j20):
    for i in range(len(j1)-1):
        m = (float(j1[i][2]))*(float(j4[i][2])) + (float(j1[i][3])*(float(j4[i][3])) + (float(j1[i][4])*(float(j4[i][4]))
        n = pow(((float(j1[i][2]))**2 + (float(j1[i][3]))**2 + (float(j1[i][4]))**2) * ((float(j4[i][2]))**2 + (float(j4[i][3]))**2 + (float(j4[i][4]))**2), 0.5)
        a_14 = acos(m/n) * 180 / math.pi
        
	print(a_14)    
                                                                                        
get_angle(a,j1,j4,j8,j12,j16,j20)
'''
'''
variable = []
num_bins = 
n,bins,patches = plt.hist(variable, num_bins, facecolor='blue', alpha=0.5)
plt.show()
'''

d_1_4 = list()
d_1_8 = list()
d_112 = list()
d_116 = list()
d_120 = list()

def get_distance(j1,j4,j8,j12,j16,j20):
    for i in range(len(j1)-1):
        d_14 = pow(((float(j1[i][2])-(float(j4[i][2])))**2 + (float(j1[i][3])-float(j4[i][3]) )**2 + (float(j1[i][4])-float(j4[i][4]) )**2), 0.5)
        d_1_4.append(d_14)
        
        d_18 = pow(((float(j1[i][2])-(float(j8[i][2])))**2 + (float(j1[i][3])-float(j8[i][3]) )**2 + (float(j1[i][4])-float(j8[i][4]) )**2), 0.5)
        d_1_8.append(d_18)
    
        d_1_12 = pow(((float(j1[i][2])-(float(j12[i][2])))**2 + (float(j1[i][3])-float(j12[i][3]) )**2 + (float(j1[i][4])-float(j12[i][4]) )**2), 0.5)
        d_112.append(d_1_12)
    
        d_1_16 = pow(((float(j1[i][2])-(float(j16[i][2])))**2 + (float(j1[i][3])-float(j16[i][3]) )**2 + (float(j1[i][4])-float(j16[i][4]) )**2), 0.5)
        d_116.append(d_1_16)
    
        d_1_20 = pow(((float(j1[i][2])-(float(j20[i][2])))**2 + (float(j1[i][3])-float(j20[i][3]) )**2 + (float(j1[i][4])-float(j20[i][4]) )**2), 0.5)
        d_120.append(d_1_20)
get_distance(j1,j4,j8, j12, j16, j20)
#print(len(d_1_8))

#plt.hist(d_1_4, bins=5)
#plt.show()
#print(bins)
#plt.hist(d_1_8, bins=5)
#plt.show()
#plt.hist(d_112, bins=5)
#plt.show()
#plt.hist(d_116, bins=5)
#plt.show()
#plt.hist(d_120, bins=5)
#plt.show()


v1r = j1
v2r = j4
vml = [[float(i) for i in j if i !="nan"] for j in v1r]
#v1j = [[int(float(k)) for k in i] for i in vml]
#v1 = [int(i) for i in v1r]
bml = vml
print((bml))
v2r = j4
v3r = j8[:][2:5]
v4r = j12[:][2:5]
v5r = j16[:][2:5]
v6r = j20[:][2:5]

a_1_4 = list()
a_1_8 = list()
a_112 = list()
a_116 = list()
a_120 = list()
'''
def unit_vector(vector):
    return vector / np.linalg.norm(vector)
 
def get_angle(v1,v2,v3,v4,v5):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    v3_u = unit_vector(v3)
    v4_u = unit_vector(v4)
    v5_u = unit_vector(v5)
    v6_u = unit_vector(v6)
    
    a_14 = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    a_1_4.append(a_14)
    print(a_1_4)
    
    a_18 = np.arccos(np.clip(np.dot(v1_u, v3_u), -1.0, 1.0))
    a_1_8.append(a_18)
    
    a_1_12 = np.arccos(np.clip(np.dot(v1_u, v3_u), -1.0, 1.0))
    a_112.append(a_1_12)
    
    a_1_16 = np.arccos(np.clip(np.dot(v1_u, v4_u), -1.0, 1.0))
    a_116.append(a_1_16)
    
    a_1_20 = np.arccos(np.clip(np.dot(v1_u, v5_u), -1.0, 1.0))
    a_120.append(a_1_20)

get_angle(v1,v2,v3,v4,v5)


'''
