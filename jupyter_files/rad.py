import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

dataset = glob.glob('dataset/train/*')
#dataset = glob.glob('dataset/test/*')
print(len(dataset))

full_frame_list = list()
for file in dataset:
    with open(file, 'r') as f:
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
        y = float(buffer_list[3])
        z = float(buffer_list[4])
        if(frame_number==this_frame):
            if(joint==1):
                buffer_dict['d1'] = [x, y, z]
                #print(buffer_dict['d1'])
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
        #print(buffer_dict['d1'])

    full_frame_list.append(frame_list)
#print(full_frame_list)

h_total = list()

for dataset in full_frame_list:
    d1 = list()
    d2 = list()
    d3 = list()
    d4 = list()
    d5 = list()
    
    t1 = list()
    t2 = list()
    t3 = list()
    t4 = list()
    t5 = list()
    
    for frame in dataset:
        for k in frame:
            d_1 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d4']))))
            d1.append((d_1))
    

            d_2 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d8']))))
            d2.append(d_2)
            d_3 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d12']))))
            d3.append(d_3)
            d_4 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d16']))))
            d4.append(d_4)
            d_5 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d20']))))
            d5.append(d_5)

            def normalize(v):
                norm = np.linalg.norm(v)
                if norm == 0: 
                    return v 
                return v / norm

            def get_angle(d1,d2,d3,d4,d5,d6):
                d1 = normalize((frame['d1']))
                d2 = normalize((frame['d4']))
                d3 = normalize((frame['d8']))
                d4 = normalize((frame['d12']))
                d5 = normalize((frame['d16']))
                d6 = normalize((frame['d20']))

                '''
                d11 = np.diff(d1,d2)
                d12 = np.diff(d1,d3)
                d13 = np.diff(d1,d4)
                d14 = np.diff(d1,d5)
                d15 = np.diff(d1,d6)
                d16 = np.diff(d6,d1)

                t_14 = np.arccos(np.clip(np.dot(d11, d12), -1.0, 1.0)) * 180 / math.pi
                t1.append(t_14)

                t_18 = np.arccos(np.clip(np.dot(d11, d13), -1.0, 1.0)) * 180 / math.pi
                t2.append(t_18)

                t_1_12 = np.arccos(np.clip(np.dot(d11, d14), -1.0, 1.0)) * 180 / math.pi
                t3.append(t_1_12)

                t_1_16 = np.arccos(np.clip(np.dot(d11, d15), -1.0, 1.0)) * 180 / math.pi
                t4.append(t_1_16)

                t_1_20 = np.arccos(np.clip(np.dot(d11, d16), -1.0, 1.0)) * 180 / math.pi
                t5.append(t_1_20)
                '''
            get_angle(np.array(frame['d1']),
                      np.array(frame['d4']),
                      np.array(frame['d8']),
                      np.array(frame['d12']),
                      np.array(frame['d16']),
                      np.array(frame['d20']))



    



        #print(t5)   
        k1 =(len(d1))
        k2 =(len(d2))
        k3 =(len(d3))
        k4 =(len(d4))
        k5 =(len(d5))

        his_d1, bin_d1 = np.histogram(d1,bins=5)
        m = [i/k1 for i in his_d1]
        hd1 = h_d1, b_d1 = m, bin_d1
        for i in range(len(h_d1)):
            freq_d1 = ((h_d1[i]))
        for i in range(len(b_d1)-1):
            binz_d1 = (b_d1[i], b_d1[i+1])
            s1 = (h_d1[i],b_d1[i],b_d1[i+1])
            h_total.append(list(s1))
            #print(list(list(s1)))

        his_d2, bin_d2 = np.histogram(d2,bins=5)
        n = [i/k2 for i in his_d2]
        hd2 = h_d2, b_d2 = (n, bin_d2)
        for i in range(len(h_d2)):
                freq_d2 = ((h_d2[i]))
        for i in range(len(b_d1)-1):
            binz_d2 = (b_d2[i], b_d2[i+1])
            s2 = (h_d2[i],b_d2[i],b_d2[i+1])
            h_total.append(list(s2))

        his_d3, bin_d3 = np.histogram(d3,bins=5)
        o = [i/k3 for i in his_d3]
        hd3 = h_d3, b_d3 = (o, bin_d3)
        for i in range(len(h_d3)):
            freq_d3 = ((h_d3[i]))
        for i in range(len(b_d1)-1):
            binz_d3 = (b_d3[i], b_d3[i+1])
            s3 = (h_d3[i],b_d3[i],b_d3[i+1])
            h_total.append(list(s3))

        his_d4, bin_d4 = np.histogram(d4,bins=5)
        p = [i/k4 for i in his_d4]
        hd4 = h_d4, b_d4 = (p, bin_d4)
        for i in range(len(h_d4)):
            freq_d4 = ((h_d4[i]))
        for i in range(len(b_d1)-1):
            binz_d4 = (b_d4[i], b_d4[i+1])
            s4 = (h_d4[i],b_d4[i],b_d4[i+1])
            h_total.append(list(s4))

        his_d5, bin_d5 = np.histogram(d5,bins=5)
        q = [i/k5 for i in his_d5]
        hd5 = h_d5, b_d5 = (q, bin_d5)
        for i in range(len(h_d5)):
            freq_d5 = ((h_d5[i]))
        for i in range(len(b_d5)-1):
            binz_d5 = (b_d5[i], b_d5[i+1])
            s5 = (h_d5[i],b_d5[i],b_d5[i+1])
            h_total.append(list(s5))

        c1 =(len(t1))
        c2 =(len(t2))
        c3 =(len(t3))
        c4 =(len(t4))
        c5 =(len(t5))

        his_t1, bin_t1 = np.histogram(t1,bins=5)
        r = [i/c1 for i in his_t1]
        ht1 = h_t1, b_t1 = (r, bin_t1)
        for i in range(len(h_t1)):
            freq_t1 = ((h_t1[i]))
        for i in range(len(b_t1)-1):
            binz_t1 = (b_t1[i], b_t1[i+1])
            s6 = (h_t1[i],b_t1[i],b_t1[i+1])
            h_total.append(list(s6))

        his_t2, bin_t2 = np.histogram(t2,bins=5)
        s = [i/c2 for i in his_t2]
        ht2 = h_t2, b_t2 = (r, bin_t2)
        for i in range(len(h_t2)):
            freq_t2 = ((h_t2[i]))
        for i in range(len(b_t2)-1):
            binz_t2 = (b_t2[i], b_t2[i+1])
            s7 = (h_t2[i],b_t2[i],b_t2[i+1])
            h_total.append(list(s7))

        his_t3, bin_t3 = np.histogram(t3,bins=5)
        t = [i/c3 for i in his_t3]
        ht3 = h_t3, b_t3 = (r, bin_t3)
        for i in range(len(h_t3)):
            freq_t3 = ((h_t3[i]))
        for i in range(len(b_t3)-1):
            binz_t3 = (b_t3[i], b_t3[i+1])
            s8 = (h_t3[i],b_t3[i],b_t3[i+1])
            h_total.append(list(s8))

        his_t4, bin_t4 = np.histogram(t4,bins=5)
        u = [i/c4 for i in his_t4]
        ht4 = h_t4, b_t4 = (r, bin_t4)
        for i in range(len(h_t4)):
            freq_t4 = ((h_t4[i]))
        for i in range(len(b_t4)-1):
            binz_t4 = (b_t4[i], b_t4[i+1])
            s9 = (h_t4[i],b_t4[i],b_t4[i+1])
            h_total.append(list(s9))

        his_t5, bin_t5 = np.histogram(t5,bins=5)
        v = [i/c5 for i in his_t5]
        ht5 = h_t5, b_t5 = (r, bin_t5)
        for i in range(len(h_t5)):
            freq_t5 = ((h_t5[i]))
        for i in range(len(b_t5)-1):
            binz_t5 = (b_t5[i], b_t5[i+1])
            s10 = (h_t5[i],b_t5[i],b_t5[i+1])
            h_total.append(list(s10))
        print(d1)
    #print(t1)
#print((h_total))
#print(len(d1))

    with open("rad_dl","w+") as f:
    #with open("rad_dl.t", "w+") as f:
        for item in h_total:
            f.write("%s\n" %item)
    f.close()
