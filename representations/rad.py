import os
import glob
import numpy as np
import math
import sys

a = sys.argv[1]
b = sys.argv[2]

if int(a) == 1:
    dataset = glob.glob('dataset/train/*.txt')
else:
    dataset = glob.glob('dataset/test/*.txt')

fileName = list()
full_frame_list = list()
for files in dataset:
    text_file = os.path.split(files)
    #print(text_file[1])
    with open(files, 'r') as f:
        train_file_read = f.readlines()
    frame_list = list()
    this_frame = 1
    buffer_dict = {
        'frame_number' : this_frame,
        'd1' : 0,
        'd4' : 0,
        'd8' : 0,
        'd12' : 0,
        'd16' : 0,
        'd20' : 0
    }
    for line in train_file_read:
        buffer_list = line.split()
        frame_number = int(buffer_list[0])
        joint = int(buffer_list[1])
        x = float(buffer_list[2])
        if math.isnan(x):
            x=0
        y = float(buffer_list[3])
        if math.isnan(y):
            y=0
        z = float(buffer_list[4])
        if math.isnan(z):
            z=0
        if(frame_number==this_frame):
            if(joint==1):
                buffer_dict['d1'] = [x, y, z]
            if(joint==4):
                buffer_dict['d4'] = [x, y, z]
            if(joint==8):
                buffer_dict['d8'] = [x, y, z]
            if(joint==12):
                buffer_dict['d12'] = [x, y, z]
            if(joint==16):
                buffer_dict['d16'] = [x, y, z]
            if(joint==20):
                buffer_dict['d20'] = [x, y, z]
        
        else:
            frame_list.append(buffer_dict)
            buffer_dict = {
                'frame_number' : frame_number,
                'd1' : [x, y, z],
                'd4' : 0,
                'd8' : 0,
                'd12' : 0,
                'd16' : 0,
                'd20' : 0
            }
            this_frame = frame_number
    fileName.append(int(text_file[1][1:3]))
    #print(fileName)
    full_frame_list.append(frame_list)

def get_distance(d,di):
    distance = (np.sum(np.square((np.array(d) - np.array(di))))) 
    return distance

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
        return v 
    return v / norm

def difference(v,vi):
    return [v[0]-vi[0], v[1]-vi[1], v[2]-vi[2]]

def get_angle(v,vi):
    v1 = normalize(v)
    v2 = normalize(vi)
    theta = np.arctan(np.clip(np.dot(v1, v2), -1.0, 1.0)) * 180 / math.pi
    return theta

def comp_hist(h):
    z = his, bin_ = np.histogram(h,bins=int(b))
    return z

joint_list = ['d4', 'd8', 'd12', 'd16', 'd20']
d_hist_list = ['d_1', 'd_2', 'd_3', 'd_4', 'd_5'] 
t_hist_list = ['t_1', 't_2', 't_3', 't_4', 't_5']
dhist = ['dh_1', 'dh_2', 'dh_3', 'dh_4', 'dh_5']
thist = ['th_1', 'th_2', 'th_3', 'th_4', 'th_5']
#print(fileName)
for file_number, filez in enumerate(full_frame_list):
    distance_dict = {}
    for item in filez:
        for k, joint in enumerate(joint_list):
            distance_key = 'd_{}'.format(k+1)
            angle_key = 't_{}'.format(k+1)
            buffer_distance = get_distance(np.array(item['d1']), np.array(item[joint]))
            if(distance_key not in distance_dict.keys()):
                distance_dict[distance_key] = [buffer_distance]
            else:
                distance_dict[distance_key].append(buffer_distance)
            if(k+1==len(joint_list)):
                buffer_angle = get_angle(difference(item['d1'], item[joint_list[k]]), \
                                         difference(item['d1'], item[joint_list[0]]))
            else:
                buffer_angle = get_angle(difference(item['d1'], item[joint_list[k]]), \
                                         difference(item['d1'], item[joint_list[k+1]]))
            if(angle_key not in distance_dict.keys()):
                distance_dict[angle_key] = [buffer_angle]
            else:
                distance_dict[angle_key].append(buffer_angle)
    l1 = (len(distance_dict[d_hist_list[0]]))
    l2 = (len(distance_dict[t_hist_list[0]]))
    
    histogram_dict = {}
    concatenate_list = list()
#Histogram for distances
    for k, h in enumerate(d_hist_list):
        d_hist_key = 'dh_{}'.format(k+1)
        buffer_hist = comp_hist(distance_dict[d_hist_list[k]])
        if(d_hist_key not in histogram_dict.keys()):
            histogram_dict[d_hist_key] = [buffer_hist]
        else:
            histogram_dict[d_hist_key].append(buffer_hist)
        d_buffer_hist = histogram_dict[dhist[k]][0][0]
        z = [x / l1 for k,x in enumerate(d_buffer_hist)]
        d_buffer_bins = histogram_dict[dhist[k]][0][1]        
        for i in range(len(z)):
            freq_d = z[i]
        for i in range(len(d_buffer_bins)-1):
            f_hist_d = v = ((z[i]))
            concatenate_list.append(f_hist_d)
#Histogram for angles
    for k, h in enumerate(t_hist_list):
        t_hist_key = 'th_{}'.format(k+1)
        buffer_hist = comp_hist(distance_dict[t_hist_list[k]])
        if(t_hist_key not in histogram_dict.keys()):
            histogram_dict[t_hist_key] = [buffer_hist]
        else:
            histogram_dict[t_hist_key].append(buffer_hist)
        t_buffer_hist = histogram_dict[thist[k]][0][0]
        y = [o / l2 for k, o in enumerate(t_buffer_hist)]
        t_buffer_bins = histogram_dict[thist[k]][0][1]
        for i in range(len(y)):
            frq_t = y[i]
        for i in range(len(t_buffer_bins)-1):
            f_hist_t = q = ((y[i]))
            concatenate_list.append(f_hist_t)
    concatenate_list = ['{}:{}'.format(k+1, str(i)) for k, i in enumerate(concatenate_list)]
    #print(fileName[file_number])
    if int(a) == 1:
        #print(fileName[file_number])
        with open('rad_d1_formated', 'a+') as f:
            if(str(fileName[file_number]) == '08'):
                n1 = ("8 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n1))

            if(str(fileName[file_number]) == '10'):
                n2 = ("10 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n2))

            if(str(fileName[file_number]) == '12'):
                n3 = ("12 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n3))

            if(str(fileName[file_number]) == '13'):
                n4 = ("13 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n4))

            if(str(fileName[file_number]) == '15'):
                n5 = ("15 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n5))

            if(str(fileName[file_number]) == '16'):
                n6 = ("16 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n6))
    else:
        with open('rad_d1_formatted.t', 'a+') as f:
            if(str(fileName[file_number]) == '08'):
                n1 = ("8 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n1))

            if(str(fileName[file_number]) == '10'):
                n2 = ("10 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n2))

            if(str(fileName[file_number]) == '12'):
                n3 = ("12 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n3))

            if(str(fileName[file_number]) == '13'):
                n4 = ("13 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n4))

            if(str(fileName[file_number]) == '15'):
                n5 = ("15 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n5))

            if(str(fileName[file_number]) == '16'):
                n6 = ("16 {}".format(' '.join(concatenate_list)))
                f.write('{}\n'.format(n6))
