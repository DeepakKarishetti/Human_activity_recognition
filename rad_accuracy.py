import subprocess
import os
import sys

cur_path = os.getcwd()

sys.path.insert(0, cur_path + '/libsvm-3.23/python')

from svmutil import *

sys.path.insert(0, cur_path + '/libsvm-3.23/tools')

from grid import *

sys.path.insert(0, cur_path)

os.system('python3 raddddd.py %d %d' %(1,8))
train_path = 'rad_d1_formated'
svm_train_path = cur_path+'/libsvm-3.23/svm-train'
gnuplot_path = '/usr/bin/gnuplot'

svm_options = ('-s %d -t %d' %(0,2))
options = ('-log2c %d,%d,%d -log2g %d,%d,%d -svmtrain %s %s -gnuplot %s -v %d' %(-5,5,1,-5,5,1,svm_train_path,svm_options,gnuplot_path,4))
p_rate, p_param = find_parameters(train_path,options)
svm_options_mod = ('-s %d -t %d -c %f -g %f' %(0,2,p_param['c'],p_param['g']))
y,x = svm_read_problem(train_path)
z = svm_train(y,x,svm_options_mod)
svm_save_model('rad_m.model',z)

os.system('python3 raddddd.py %d %d' %(0,5))
test_path = 'rad_d1_formatted.t'
y, x = svm_read_problem(test_path)
zz = svm_load_model('rad_m.model')
p_labels, p_acc, p_vals = svm_predict(y,x,zz)
evaluations(y, p_labels)
