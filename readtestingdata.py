# -*- coding: utf-8
# !/usr/bin/env python

import pandas as pd
import numpy as np
import csv


w = np.load('model.npy')

test_x = []
with open('test.csv') as file:
    data = file.read()
    file.close()
list = data.split('\n')

for i in range((len(list)-1)/18):
    test_x.append([])
    for j in range(18):
        for r in range(2, 11):
            if list[18*i+j].split(',')[r] != 'NR':
                test_x[i].append(float(list[18*i+j].split(',')[r]))
            else:
                test_x[i].append(0)
test_x = np.array(test_x)
# add bias
test_x = np.concatenate((np.ones((test_x.shape[0],1)), test_x), axis=1)
# print test_x.shape

# get ans.csv with the model
ans = []
for i in range(len(test_x)):
    ans.append(['id_'+str(i)])
    a = np.dot(w, test_x[i])
    ans[i].append(a)

filename = 'predict.csv'
with open(filename, 'a') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'value'])
    for i in range(len(ans)):
        writer.writerow(ans[i])
    file.close()
