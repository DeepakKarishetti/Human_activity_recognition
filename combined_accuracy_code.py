'''

CSCI 573
Deepak Rajasekhar Karishetti
10846936

'''


#import modules
import os
import sys
import numpy as np
#defining the current directory path
cur_path = os.getcwd()

#importing the libsvm python functions
sys.path.insert(0, cur_path + '/libsvm-3.23/python')

from svmutil import *
sys.path.insert(0, cur_path + '/libsvm-3.23/tools')
from grid import *
sys.path.insert(0, cur_path)

#Defining the input argument for the respective representations
a = sys.argv[1]

#For RAD representation 
if(int(a) == 1):
    os.system('python3 raddddd.py %d %d' %(1,5))
    train_path = 'rad_d1_formated'
    svm_train_path = cur_path+'/libsvm-3.23/svm-train'
    gnuplot_path = '/usr/bin/gnuplot'
    svm_options = ('-s %d -t %d' %(0,2))
    options = ('-log2c %d,%d,%d -log2g %d,%d,%d -svmtrain %s %s -gnuplot %s -v %d' %(-5,5,1,-5,5,1,svm_train_path,svm_options,gnuplot_path,5))
    p_rate, p_param = find_parameters(train_path,options)
    svm_options_mod = ('-s %d -t %d -c %f -g %f' %(0,2,p_param['c'],p_param['g']))
    y,x = svm_read_problem(train_path)
    z_m = svm_train(y,x,svm_options_mod)
    svm_save_model('rad_m.model',z_m)
    os.system('python3 raddddd.py %d %d' %(0,5))
    test_path = 'rad_d1_formatted.t'
    y, x = svm_read_problem(test_path)
    zz = svm_load_model('rad_m.model')
    p_labels, p_acc, p_vals = svm_predict(y,x,zz)
    evaluations(y, p_labels)

    y,x = svm_read_problem(test_path)
    a = svm_load_model('rad_m.model')
    p_labels, p_acc, p_vals = svm_predict(y, x, z_m)
    p, q, r = evaluations(y, p_labels)
    ini = (6,6)
    matrix = np.zeros(ini)
    act = [8, 10, 12, 13, 15, 16]
    for i in range(len(y)):
        for j in range(len(act)):
            if y[i] == act[j]:
                for k in range(len(act)):
                    if p_labels[i] == act[k]:
                        matrix[j][k] = matrix[j][k]+1 
    print(matrix)




#for HJPD representation
elif(int(a) == 2):
    os.system('python3 hjpddddd.py %d %d' %(1,4))
    train_path = 'hjpd_d1_formated'
    svm_train_path = cur_path+'/libsvm-3.23/svm-train'
    gnuplot_path = '/usr/bin/gnuplot'
    svm_options = ('-s %d -t %d' %(0,2))
    options = ('-log2c %d,%d,%d -log2g %d,%d,%d -svmtrain %s %s -gnuplot %s -v %d' %(-7,7,1,-7,7,1,svm_train_path,svm_options,gnuplot_path,4))
    p_rate, p_param = find_parameters(train_path,options)
    svm_options_mod = ('-s %d -t %d -c %f -g %f' %(0,2,p_param['c'],p_param['g']))
    y,x = svm_read_problem(train_path)
    z_m = svm_train(y,x,svm_options_mod)
    svm_save_model('hjpd_m.model',z_m)
    os.system('python3 hjpddddd.py %d %d' %(0,4))
    test_path = 'hjpd_d1_formated.t'
    y, x = svm_read_problem(test_path)
    zz = svm_load_model('hjpd_m.model')
    p_labels, p_acc, p_vals = svm_predict(y,x,zz)
    evaluations(y, p_labels)

    y,x = svm_read_problem(test_path)
    a = svm_load_model('rad_m.model')
    p_labels, p_acc, p_vals = svm_predict(y, x, z_m)
    p, q, r = evaluations(y, p_labels)
    ini = (6,6)
    matrix = np.zeros(ini)
    act = [8, 10, 12, 13, 15, 16]
    for i in range(len(y)):
        for j in range(len(act)):
            if y[i] == act[j]:
                for k in range(len(act)):
                    if p_labels[i] == act[k]:
                        matrix[j][k] = matrix[j][k]+1 
    print(matrix)

#for HOD representation
elif(int(a) == 3):
    os.system('python3 hoddddd.py %d' %(1))
    train_path = 'hod_d1_formated'
    svm_train_path = cur_path+'/libsvm-3.23/svm-train'
    gnuplot_path = '/usr/bin/gnuplot'
    svm_options = ('-s %d -t %d' %(0,2))
    options = ('-log2c %d,%d,%d -log2g %d,%d,%d -svmtrain %s %s -gnuplot %s -v %d' %(-2,2,1,-2,2,1,svm_train_path,svm_options,gnuplot_path,4))
    p_rate, p_param = find_parameters(train_path,options)
    svm_options_mod = ('-s %d -t %d -c %f -g %f' %(0,2,p_param['c'],p_param['g']))
    y,x = svm_read_problem(train_path)
    z_m = svm_train(y,x,svm_options_mod)
    svm_save_model('rad_m.model',z_m)
    os.system('python3 hoddddd.py %d' %(0))
    test_path = 'hod_d1_formated.t'
    y, x = svm_read_problem(test_path)
    zz = svm_load_model('rad_m.model')
    p_labels, p_acc, p_vals = svm_predict(y,x,zz)
    evaluations(y, p_labels)
    y,x = svm_read_problem(test_path)
    a = svm_load_model('rad_m.model')
    p_labels, p_acc, p_vals = svm_predict(y, x, z_m)
    p, q, r = evaluations(y, p_labels)
    ini = (6,6)
    matrix = np.zeros(ini)
    act = [8, 10, 12, 13, 15, 16]
    for i in range(len(y)):
        for j in range(len(act)):
            if y[i] == act[j]:
                for k in range(len(act)):
                    if p_labels[i] == act[k]:
                        matrix[j][k] = matrix[j][k]+1 
    print(matrix)

