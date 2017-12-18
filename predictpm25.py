# -*- coding: utf-8
# !/usr/bin/env python

import pandas as pd
import numpy as np
from numpy.linalg import inv
import random
import math
import sys
import csv


# read data
train_data = []
# Taiwan encoding big5
# data = pd.read_csv('train.csv', encoding='big5')
# for i in range(len(data)):
#     for j in range(3,27):
#         if data.iloc[i,j] != "NR":
#             data.iloc[i,j] = float(data.iloc[i,j])
#         else:
#             data.iloc[i,j] = float(0)
for i in range(18):
    train_data.append([])
n_row = 1
data = pd.read_csv('train.csv', encoding='big5')
for r in range(len(data)):
    for i in range(3, 27):
        if data.iloc[r, i] != "NR":
            train_data[(n_row-1)%18].append(float(data.iloc[r, i]))
        else:
            train_data[(n_row-1)%18].append(float(0))
    n_row += 1
# print train_data

# parse data to (x, y)
x = []
y = []
# 每12个月
for i in range(12):
    # 每月连续10小时的有471笔
    for j in range(471):
        x.append([])
        # 18种污染物
        for t in range(18):
            # 连续9小时
            for s in range(9):
                x[471*i+j].append(train_data[t][480*i+j+s])
        y.append(train_data[9][480*i+j+9])
x = np.array(x)
y = np.array(y)
# add bias
x = np.concatenate((np.ones((x.shape[0], 1)),x), axis=1)
print x.shape # (5652,163)
print y.shape # (562,)

w = np.zeros(len(x[0]))
l_rate = 10
repeat = 10000

# start training
# 改变维度,有参数的话按照参数换,没有则倒置
# x_t = x.transpose()
# s_gra = np.zeros(len(x[0]))
#
# for i in range(repeat):
#     hypo = np.dot(x, w)
#     loss = hypo - y
#     cost = np.sum(loss**2)/len(x)
#     cost_a = math.sqrt(cost)
#     gra = np.dot(x_t, loss)
#     s_gra += gra**2
#     ada = np.sqrt(s_gra)
#     w = w - l_rate*gra/ada
#     print 'iteration: %d | Cost: %f' % (i, cost_a)
#
# np.save('model.npy', w)