'''
Multiple layer perception Neural Network
Input from CSV file
Dynamic for hidden layer and output 

                                                                1-5-2014
                                                                By.Aldy syahdeini
'''


import numpy as nm
import csv
import heapq
import collections
from cmath import sqrt
from math import pow
import matplotlib.pyplot as plt
from random import uniform

# Constant (dynamic)
input_file="dataKnn.csv"
N_hid_layer=4
N_out_layer=1
MIN_weight=1
MAX_weight=1

# return data_raw => list of data
def csv_reader(file_obj):
    reader = csv.reader(file_obj, dialect=csv.excel_tab)
    data = []
    for row in reader:
        data.append(row[0].split(','))
    return data

def kupas_data(raw_data):
    kelas=list()
    for i,data in enumerate(raw_data):
        kelas.append(data[-1])
        raw_data[i]=data[:-1]
    return raw_data,kelas


###############################
## INIT #######################
###############################
dataSet = []

weight_list=[]
with open(input_file, "rU") as f_obj:
    dataSet = csv_reader(f_obj)

dataSet,kelasSet=kupas_data(dataSet)
weight_list=[[list() for r in range(N_hid_layer)] for i in range(len(dataSet[0]))] # with W0

# select random weight
for i,one_input in enumerate(weight_list):
    for j,one_val in enumerate(one_input):
        weight_list[i][j]=uniform(MIN_weight,MAX_weight)

weight_hid_list=[[list() for i in range(N_out_layer)] for j in range(N_hid_layer)]
for i in range(N_hid_layer):
    for j in range(N_out_layer):
        weight_hid_list[i][j]=uniform(MIN_weight,MAX_weight)


###########################################
#iterate until EPOCH #####################
##########################################
EPOCH=1
for x in range(EPOCH):
    # iterate through whole data in dataset
    for i,row_data in enumerate(dataSet):
        # initialize list for Oh and Oy
        Oh=[list() for i in range(N_hid_layer)]
        Oy=[list() for i in range(N_out_layer)]
        # print 'Oh',Oy

    ##############################
    # feed forward ###############
    ###############################
        # calculate Oh
        for k,data in enumerate(row_data): #in one data float
            for j in range(N_hid_layer):
                if Oh[j]==[]:
                    Oh[j]=0
                Oh[j]+=weight_list[k][j]*float(data)
        # calculate Ok
        for k in range(N_hid_layer):
            for j in range(len(Oy)):
                if Oy[j]==[]:
                    Oy[j]=0
                Oy[j]+=weight_hid_list[k][j]*Oh[k]

        # get error
        Ey=[ list() for i in range(len(Oy))]
        for k in range(len(Oy)):
            temp_error=0
            # get error K
            Ey[k]=Oy[k]*(1-Oy[k])*(int(kelasSet[i])-Oy[k])


        ####################################
        # back propagation#################
        ####################################
        for k,w in enumerate(Oh):
            for z,o in enumerate(Oy):
                # update weight hidden
                delta_w=0.05*weight_hid_list[k][z]*Ey[z]
                weight_hid_list[k][z]+=delta_w

        for i,j in enumerate(row_data):
            for k,l in enumerate(Oh):
                # update weight
                delta_w=0.05*weight_list[i][k]*Oh[k]
                weight_list[i][k]+=delta_w

######### END OF EPOCH ###############################

print weight_list




















