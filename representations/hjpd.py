import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import math
import sys


a = sys.argv[1]
b = sys.argv[2]

if int(a) == 1:
    dataset = glob.glob('dataset/train/*')
else:
    dataset = glob.glob('dataset/test/*')

fileName = list()
full_frame_list = list()
for files in dataset:
    text_file = os.path.split(files)
    with open(files, 'r') as f:
        train_file_read = f.readlines()
    frame_list = list()
    this_frame = 1
    buffer_dict = {
        'frame_number' : this_frame,
        'd1' : 0,
        'd2' : 0,
        'd3' : 0,
        'd4' : 0,
        'd5' : 0,
        'd6' : 0,
        'd7' : 0,
        'd8' : 0,
        'd9' : 0,
        'd10' : 0,
        'd11' : 0,
        'd12' : 0,
        'd13' : 0,
        'd14' : 0,
        'd15' : 0,
        'd17' : 0,
        'd18' : 0,
        'd19' : 0,
        'd20' : 0,
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
            if(joint==2):
                buffer_dict['d2'] = [x, y, z]
            if(joint==3):
                buffer_dict['d3'] = [x, y, z]
            if(joint==4):
                buffer_dict['d4'] = [x, y, z]
            if(joint==5):
                buffer_dict['d5'] = [x, y, z]
            if(joint==6):
                buffer_dict['d6'] = [x, y, z]
            if(joint==7):
                buffer_dict['d7'] = [x, y, z]
            if(joint==8):
                buffer_dict['d8'] = [x, y, z]
            if(joint==9):
                buffer_dict['d9'] = [x, y, z]
            if(joint==10):
                buffer_dict['d10'] = [x, y, z]
            if(joint==11):
                buffer_dict['d11'] = [x, y, z]
            if(joint==12):
                buffer_dict['d12'] = [x, y, z]
            if(joint==13):
                buffer_dict['d13'] = [x, y, z]
            if(joint==14):
                buffer_dict['d14'] = [x, y, z]
            if(joint==15):
                buffer_dict['d15'] = [x, y, z]
            if(joint==16):
                buffer_dict['d16'] = [x, y, z]
            if(joint==17):
                buffer_dict['d17'] = [x, y, z]
            if(joint==18):
                buffer_dict['d18'] = [x, y, z]
            if(joint==19):
                buffer_dict['d19'] = [x, y, z]
            if(joint==20):
                buffer_dict['d20'] = [x, y, z]
        else:
            frame_list.append(buffer_dict)
            buffer_dict = {
                'frame_number' : frame_number,
                'd1' : [x, y, z],
                'd2' : 0,
                'd3' : 0,
                'd4' : 0,
                'd5' : 0,
                'd6' : 0,
                'd7' : 0,
                'd8' : 0,
                'd9' : 0,
                'd11' : 0,
                'd12' : 0,
                'd13' : 0,
                'd14' : 0,
                'd15' : 0,
                'd16' : 0,
                'd17' : 0,
                'd18' : 0,
                'd19' : 0,
                'd20' : 0,
            }
            this_frame = frame_number
    fileName.append(int(text_file[1][1:3]))
    full_frame_list.append(frame_list)

def get_displacement(d,di):
    displacement = (np.array(d) - np.array(di))
    return displacement

def comp_hist(h):
    z = his, bin_ = np.histogram(h,bins=int(b))
    return z

joint_list = ['d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13','d14','d15','d16','d17','d18','d19','d20']
disp_hist_list = ['d_1','d_2','d_3','d_4','d_5','d_6','d_7','d_8','d_9','d_10','d_11','d_12','d_13','d_14','d_15','d_16','d_17','d_18','d_19']
dhist = ['dh_1','dh_2','dh_3','dh_4','dh_5','dh_6','dh_7','dh_8','dh_9','dh_10','dh_11','dh_12','dh_13','dh_14','dh_15','dh_16','dh_17','dh_18','dh_19']

for file_number, filez in enumerate(full_frame_list):
    displacement_dict = {}
    for item in filez:
        for k, joint in enumerate(joint_list):
            displacement_key = 'd_{}'.format(k+1)
            
            buffer_displacement = get_displacement(np.array(item['d1']), np.array(item[joint]))
            if(displacement_key not in displacement_dict.keys()):
                displacement_dict[displacement_key] = [buffer_displacement]
            else:
                displacement_dict[displacement_key].append(buffer_displacement)
    l1 = len(displacement_dict[disp_hist_list[0]])
    
    histogram_dict = {}
    concatenate_list = list()
#Histogram for displacements
    for k, h in enumerate(disp_hist_list):
        d_hist_key = 'dh_{}'.format(k+1)
        buffer_hist = comp_hist(displacement_dict[disp_hist_list[k]])
        
        if(d_hist_key not in histogram_dict.keys()):
            histogram_dict[d_hist_key] = [buffer_hist]
        else:
            histogram_dict[d_hist_key].append(buffer_hist)
                    
        disp_buffer_hist = histogram_dict[dhist[k]][0][0]
        z = [x / l1 for k, x in enumerate(disp_buffer_hist)]
        disp_buffer_bins = histogram_dict[dhist[k]][0][1]
        for i in range(len(z)):
            freq_disp = z[i]
        for i in range(len(disp_buffer_bins)-1):
            f_hist_disp = v = ((z[i]))
            concatenate_list.append(f_hist_disp)
    
    concatenate_list = ['{}:{}'.format(k+1, str(i)) for k, i in enumerate(concatenate_list)]
    
    if int(a) == 1:
        with open('hjpd_d1_formated', 'a+') as f:
            
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
        with open('hjpd_d1_formated.t', 'a+') as f:
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

