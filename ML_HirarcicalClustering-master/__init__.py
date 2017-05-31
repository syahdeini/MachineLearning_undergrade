"""----------------------
    Hirarcical Clustering
    ---------------------
    Using dictionary
                                13-Mei-2014 13:33
                                Aldy syahdeini
"""

import csv
from math import sqrt

def csv_reader(file_obj):
    reader=csv.reader(file_obj,dialect=csv.excel_tab)
    data=[]
    for row in reader:
        data.append(row[0].split(','))
    return data
    #print reader[0]


def ed(data1,data2):
    sum=0
    for i in range(len(data1)):
        sum+=pow(float(data1[i])-float(data2[i]),2)
    return abs(sqrt(sum))

def calculate_centroid(data1,data2):
    temp_data=list()
    for i,data in enumerate(data1):
        temp_data.append((float(data1[i])+float(data2[i]))/2)
    return temp_data

with open("clusterF.csv","rU") as f_obj:
    dataSet=csv_reader(f_obj)

'''
var_list=[list() for i in range(len(dataSet))]
#initialize var list
for i in range(len(dataSet)):
#    var_list.append(list())
    var_list[i].append(i)

print var_list
'''



point_dict=dict()
for i in range(len(dataSet)):
    point_dict.update({str(i+1):dataSet[i]})
print 'data awal ',point_dict





for i in range(len(dataSet)-1):
    ed_dict=dict()
    min_ed=10000
    for key1 in point_dict:
        for key2 in point_dict:
            if(ed(point_dict[key1],point_dict[key2])<min_ed and key1!=key2):
                keyTemp1=key1
                keyTemp2=key2


    print keyTemp1,keyTemp2,' di gabung'
    print '================================================='
    print
    point_dict.update({str(keyTemp1)+'+'+str(keyTemp2):calculate_centroid(point_dict[keyTemp1],point_dict[keyTemp2])})
    del point_dict[keyTemp1]
    del point_dict[keyTemp2]
    print 'data now = ',point_dict

