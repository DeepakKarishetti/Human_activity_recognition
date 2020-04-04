import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

dataset = glob.glob('dataset/train/*')
#dataset = glob.glob('dataset/test/*')
#print(len(dataset))

full_frame_list = list()
for file in dataset:
    with open(file, 'r') as f:
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
        'd16' : 0,
        'd17' : 0,
        'd18' : 0,
        'd19' : 0,
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
            if(joint==2):
                buffer_dict['d1'] = [x, y, z]
            if(joint==3):
                buffer_dict['d1'] = [x, y, z]
            if(joint==4):
                buffer_dict['d1'] = [x, y, z]
            if(joint==5):
                buffer_dict['d1'] = [x, y, z]
            if(joint==6):
                buffer_dict['d1'] = [x, y, z]
            if(joint==7):
                buffer_dict['d1'] = [x, y, z]
            if(joint==8):
                buffer_dict['d1'] = [x, y, z]
            if(joint==9):
                buffer_dict['d1'] = [x, y, z]
            if(joint==10):
                buffer_dict['d1'] = [x, y, z]
            if(joint==11):
                buffer_dict['d1'] = [x, y, z]
            if(joint==12):
                buffer_dict['d1'] = [x, y, z]
            if(joint==13):
                buffer_dict['d1'] = [x, y, z]
            if(joint==14):
                buffer_dict['d1'] = [x, y, z]
            if(joint==15):
                buffer_dict['d1'] = [x, y, z]
            if(joint==16):
                buffer_dict['d4'] = [x, y, z]
            if(joint==17):
                buffer_dict['d8'] = [x, y, z]
            if(joint==18):
                buffer_dict['d12'] = [x, y, z]
            if(joint==19):
                buffer_dict['d16'] = [x, y, z]
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
                'd10' : 0,
                'd11' : 0,
                'd12' : 0,
                'd13' : 0,
                'd14' : 0,
                'd15' : 0,
                'd16' : 0,
                'd17' : 0,
                'd18' : 0,
                'd19' : 0,
                'd20' : 0
            }
            this_frame = frame_number
        #print(((buffer_dict['d1'])))

    full_frame_list.append(frame_list)
print(len(full_frame_list))

h_total = list()
for dataset in full_frame_list:
    #d_trial = list()
    d1 = list()
    d2 = list()
    d3 = list()
    d4 = list()
    d5 = list()
    d6 = list()
    d7 = list()
    d8 = list()
    d9 = list()
    d10 = list()
    d11 = list()
    d12 = list()
    d13 = list()
    d14 = list()
    d15 = list()
    d16 = list()
    d17 = list()
    d18 = list()
    d19 = list()
    d20 = list()
    
    for frame in dataset:
        d_1 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d1']))))
        d1.append((d_1))
        d_2 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d2']))))
        d2.append(d_2)
        d_3 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d3']))))
        d3.append(d_3)
        d_4 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d4']))))
        d4.append(d_4)
        d_5 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d5']))))
        d5.append(d_5)
        d_6 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d6']))))
        d6.append((d_6))
        d_7 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d7']))))
        d7.append(d_7)
        d_8 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d8']))))
        d8.append(d_8)
        d_9 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d9']))))
        d9.append(d_9)
        d_10 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d10']))))
        d10.append(d_10)
        d_11 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d11']))))
        d11.append((d_11))
        d_12 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d12']))))
        d12.append(d_12)
        d_13 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d13']))))
        d13.append(d_13)
        d_14 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d14']))))
        d14.append(d_14)
        d_15 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d15']))))
        d15.append(d_15)
        d_16 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d16']))))
        d16.append((d_16))
        d_17 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d17']))))
        d17.append(d_17)
        d_18 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d18']))))
        d18.append(d_18)
        d_19 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d19']))))
        d19.append(d_19)
        d_20 = (np.sum(np.square(np.array(frame['d1'])-np.array(frame['d20']))))
        d20.append(d_20)
    #print(d1)
    
'''k1 = len(d1)
    k2 =(len(d2))
    k3 =(len(d3))
    k4 =(len(d4))
    k5 =(len(d5))
    k6 =(len(d1))
    k7 =(len(d2))
    k8 =(len(d3))
    k9 =(len(d4))
    k10 =(len(d5))
    k11 =(len(d1))
    k12 =(len(d2))
    k13 =(len(d3))
    k14 =(len(d4))
    k15 =(len(d5))
    k16 = len(d1)
    k17 =(len(d2))
    k18 =(len(d3))
    k19 =(len(d4))
    k20 =(len(d5))
    #print(k1)
    
    his_d1, bin_d1 = np.histogram(d1,bins=5)
    m1 = [i/k1 for i in his_d1]
    hd1 = h_d1, b_d1 = m1, bin_d1
    for i in range(len(h_d1)):
        freq_d1 = ((h_d1[i]))
    for i in range(len(b_d1)-1):
        binz_d1 = (b_d1[i], b_d1[i+1])
        s1 = (h_d1[i],b_d1[i],b_d1[i+1])
        h_total.append(list(s1))
        #print(list(s1))
        
        

    his_d2, bin_d2 = np.histogram(d2,bins=5)
    m2 = [i/k2 for i in his_d2]
    hd2 = h_d2, b_d2 = m2, bin_d2
    for i in range(len(h_d2)):
        freq_d2 = ((h_d2[i]))
    for i in range(len(b_d2)-1):
        binz_d2 = (b_d2[i], b_d2[i+1])
        s2 = (h_d2[i],b_d2[i],b_d2[i+1])
        h_total.append(list(s2))
        
    his_d3, bin_d3 = np.histogram(d3,bins=5)
    m3 = [i/k3 for i in his_d3]
    hd3 = h_d3, b_d3 = m3, bin_d3
    for i in range(len(h_d3)):
        freq_d3 = ((h_d3[i]))
    for i in range(len(b_d3)-1):
        binz_d3 = (b_d3[i], b_d3[i+1])
        s3 = (h_d3[i],b_d3[i],b_d3[i+1])
        h_total.append(list(s3))
        
    his_d4, bin_d4 = np.histogram(d4,bins=5)
    m4 = [i/k4 for i in his_d4]
    hd4 = h_d4, b_d4 = m4, bin_d4
    for i in range(len(h_d4)):
        freq_d4 = ((h_d4[i]))
    for i in range(len(b_d4)-1):
        binz_d4 = (b_d4[i], b_d4[i+1])
        s4 = (h_d4[i],b_d4[i],b_d4[i+1])
        h_total.append(list(s4))
        
    his_d5, bin_d5 = np.histogram(d5,bins=5)
    m5 = [i/k5 for i in his_d5]
    hd5 = h_d5, b_d5 = m5, bin_d5
    for i in range(len(h_d5)):
        freq_d5 = ((h_d5[i]))
    for i in range(len(b_d5)-1):
        binz_d5 = (b_d5[i], b_d5[i+1])
        s5 = (h_d5[i],b_d5[i],b_d5[i+1])
        h_total.append(list(s5))
        
    his_d6, bin_d6 = np.histogram(d6,bins=5)
    m6 = [i/k6 for i in his_d6]
    hd6 = h_d6, b_d6 = m6, bin_d6
    for i in range(len(h_d6)):
        freq_d6 = ((h_d6[i]))
    for i in range(len(b_d6)-1):
        binz_d6 = (b_d6[i], b_d6[i+1])
        s6 = (h_d6[i],b_d6[i],b_d6[i+1])
        h_total.append(list(s6))
        
    his_d7, bin_d7 = np.histogram(d7,bins=5)
    m7 = [i/k7 for i in his_d7]
    hd7 = h_d7, b_d7 = m7, bin_d7
    for i in range(len(h_d7)):
        freq_d7 = ((h_d7[i]))
    for i in range(len(b_d7)-1):
        binz_d7 = (b_d7[i], b_d7[i+1])
        s7 = (h_d7[i],b_d7[i],b_d7[i+1])
        h_total.append(list(s7))
        
    his_d8, bin_d8 = np.histogram(d8,bins=5)
    m8 = [i/k8 for i in his_d8]
    hd8 = h_d8, b_d8 = m8, bin_d8
    for i in range(len(h_d8)):
        freq_d8 = ((h_d8[i]))
    for i in range(len(b_d8)-1):
        binz_d8 = (b_d8[i], b_d8[i+1])
        s8 = (h_d8[i],b_d8[i],b_d8[i+1])
        h_total.append(list(s8))
        
    his_d9, bin_d9 = np.histogram(d9,bins=5)
    m9 = [i/k9 for i in his_d9]
    hd9 = h_d9, b_d9 = m9, bin_d9
    for i in range(len(h_d9)):
        freq_d9 = ((h_d9[i]))
    for i in range(len(b_d9)-1):
        binz_d9 = (b_d9[i], b_d9[i+1])
        s9 = (h_d9[i],b_d9[i],b_d9[i+1])
        h_total.append(list(s9))
        
    his_d10, bin_d10 = np.histogram(d10,bins=5)
    m10 = [i/k10 for i in his_d10]
    hd10 = h_d10, b_d10 = m10, bin_d10
    for i in range(len(h_d10)):
        freq_d10 = ((h_d10[i]))
    for i in range(len(b_d10)-1):
        binz_d10 = (b_d10[i], b_d10[i+1])
        s10 = (h_d10[i],b_d10[i],b_d10[i+1])
        h_total.append(list(s10))
        
    his_d11, bin_d11 = np.histogram(d11,bins=5)
    m11 = [i/k11 for i in his_d11]
    hd11 = h_d11, b_d11 = m11, bin_d11
    for i in range(len(h_d11)):
        freq_d11 = ((h_d11[i]))
    for i in range(len(b_d11)-1):
        binz_d11 = (b_d11[i], b_d11[i+1])
        s11 = (h_d11[i],b_d11[i],b_d11[i+1])
        h_total.append(list(s11))
        #print(list(s1))
        
    his_d12, bin_d12 = np.histogram(d12,bins=5)
    m12 = [i/k12 for i in his_d12]
    hd12 = h_d12, b_d12 = m12, bin_d12
    for i in range(len(h_d12)):
        freq_d12 = ((h_d12[i]))
    for i in range(len(b_d12)-1):
        binz_d12 = (b_d12[i], b_d12[i+1])
        s12 = (h_d12[i],b_d12[i],b_d12[i+1])
        h_total.append(list(s12))
        
    his_d13, bin_d13 = np.histogram(d13,bins=5)
    m13 = [i/k13 for i in his_d13]
    hd13 = h_d13, b_d13 = m13, bin_d13
    for i in range(len(h_d13)):
        freq_d13 = ((h_d13[i]))
    for i in range(len(b_d13)-1):
        binz_d13 = (b_d13[i], b_d13[i+1])
        s13 = (h_d13[i],b_d13[i],b_d13[i+1])
        h_total.append(list(s13))
        
    his_d14, bin_d14 = np.histogram(d14,bins=5)
    m14 = [i/k14 for i in his_d14]
    hd14 = h_d14, b_d14 = m14, bin_d14
    for i in range(len(h_d14)):
        freq_d14 = ((h_d14[i]))
    for i in range(len(b_d14)-1):
        binz_d14 = (b_d14[i], b_d14[i+1])
        s14 = (h_d14[i],b_d14[i],b_d14[i+1])
        h_total.append(list(s14))
        
    his_d15, bin_d15 = np.histogram(d15,bins=5)
    m15 = [i/k15 for i in his_d15]
    hd15 = h_d15, b_d15 = m15, bin_d15
    for i in range(len(h_d15)):
        freq_d15 = ((h_d15[i]))
    for i in range(len(b_d15)-1):
        binz_d15 = (b_d15[i], b_d15[i+1])
        s15 = (h_d15[i],b_d15[i],b_d15[i+1])
        h_total.append(list(s15))
        
    his_d16, bin_d16 = np.histogram(d16,bins=5)
    m16 = [i/k16 for i in his_d16]
    hd16 = h_d16, b_d16 = m16, bin_d16
    for i in range(len(h_d16)):
        freq_d16 = ((h_d16[i]))
    for i in range(len(b_d16)-1):
        binz_d16 = (b_d16[i], b_d16[i+1])
        s16 = (h_d16[i],b_d16[i],b_d16[i+1])
        h_total.append(list(s16))
        
    his_d17, bin_d17 = np.histogram(d17,bins=5)
    m17 = [i/k17 for i in his_d17]
    hd17 = h_d17, b_d17 = m17, bin_d17
    for i in range(len(h_d17)):
        freq_d17 = ((h_d17[i]))
    for i in range(len(b_d17)-1):
        binz_d17 = (b_d17[i], b_d17[i+1])
        s17 = (h_d17[i],b_d17[i],b_d17[i+1])
        h_total.append(list(s17))
        
    his_d18, bin_d18 = np.histogram(d18,bins=5)
    m18 = [i/k18 for i in his_d18]
    hd18 = h_d18, b_d18 = m18, bin_d18
    for i in range(len(h_d18)):
        freq_d18 = ((h_d18[i]))
    for i in range(len(b_d18)-1):
        binz_d18 = (b_d18[i], b_d18[i+1])
        s18 = (h_d18[i],b_d18[i],b_d18[i+1])
        h_total.append(list(s18))
        
    his_d19, bin_d19 = np.histogram(d19,bins=5)
    m19 = [i/k19 for i in his_d19]
    hd19 = h_d19, b_d19 = m19, bin_d19
    for i in range(len(h_d19)):
        freq_d19 = ((h_d19[i]))
    for i in range(len(b_d19)-1):
        binz_d19 = (b_d19[i], b_d19[i+1])
        s19 = (h_d19[i],b_d19[i],b_d19[i+1])
        h_total.append(list(s19))
        
    his_d20, bin_d20 = np.histogram(d20,bins=5)
    m20 = [i/k20 for i in his_d20]
    hd20 = h_d20, b_d20 = m20, bin_d20
    for i in range(len(h_d20)):
        freq_d20 = ((h_d20[i]))
    for i in range(len(b_d20)-1):
        binz_d20 = (b_d20[i], b_d20[i+1])
        s20 = (h_d20[i],b_d20[i],b_d20[i+1])
        h_total.append(list(s20))
        
print(len(h_total))
   ''' 
