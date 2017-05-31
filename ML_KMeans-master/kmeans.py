'''
Created on Apr 1, 2014

K-Means with plot,
plot using matplotlib


@author: Aldy syahdeini
'''

import csv
import collections
from cmath import sqrt
from math import pow
import matplotlib.pyplot as plt



fileName="clusterC.csv"
MAX=1000000




#finding eucledian distance between one row data
def ed(data1,data2):
    sum=0
    for i in range(len(data1)):
        sum+=pow(float(data1[i])-float(data2[i]),2)
    return abs(sqrt(sum))

# reading CSV file
def csv_reader(file_obj):
    reader=csv.reader(file_obj,dialect=csv.excel_tab)
    data=[]
    for row in reader:
        data.append(row[0].split(','))
    return data
    #print reader[0]

#### MAIN ##############################
dataSet=[]        
with open(fileName,"rU") as f_obj:
    dataSet=csv_reader(f_obj)
    
K=raw_input("enter K value : ")
K=int(K)

#find centroid
dataSet_len=len(dataSet)
centroid=[]
for i in range(K):
    centroid.append(list(dataSet[int(dataSet_len/K)*i]))

##########################################################################
##### Iterating until confindent (previous centroid == current centroid)##
##########################################################################
while True:
    # # initialize cluster and distance for each data
    cluster=[]
    distance=[]
    for i in range(len(dataSet)):
        cluster.append(0)
        distance.append(MAX)
             
                
        #find a cluster
    for cent in centroid:
        for i in range(len(dataSet)):
            # get Eucledian distance between centroid and data
            eucl_dist=ed(cent,dataSet[i])
            if eucl_dist<distance[i]:
                cluster[i]=centroid.index(cent)
                distance[i]=eucl_dist
    
                
    list_update_centroid=[[] for i in range(K)]    
    for i in range(len(dataSet)):
        list_update_centroid[cluster[i]].append(list(dataSet[i]))
         
   
    save_centroid=[]      
    #save_centroid=list(centroid) 
    for data in centroid:
        save_centroid.append(list(data))
    save_list_centroid=list_update_centroid[:]
        
    #reset centroid 
    for troid in centroid:
        for i in range(len(troid)):
             troid[i]=0
 
    # update centroid (sum each variable)
    for i in range(len(list_update_centroid)):
             #get one cluster
             cluster=i
             for data in list_update_centroid[i] :
             #iterato in one data in one cluster
                for i in range(len(data)):
                     centroid[cluster][i]+=float(data[i])
    
    
    # divide each variable by N
    for i in range(len(centroid)):
        for j in range(len(data)):
            centroid[i][j]=centroid[i][j]/len(list_update_centroid[i])
    
    print '------------'
    print save_list_centroid
    print centroid
    if save_centroid==centroid:  # test confidential
        break
    


print "----- END RESULT ------"
for i in range(len(centroid)):
    print 'centroid ',i,centroid[i]
for i in range(len(save_list_centroid)):
    print 'cluster ',i,save_list_centroid[i]

###############################################
#### FOR PLOTTING ############################
##############################################

linespec=['ro','go','bo','co','mo','yo','ko','wo'] # color for plot
X1=[]
Y1=[]
for i in range(len(save_list_centroid)):
    X=[]
    Y=[]
    for dataList in save_list_centroid[i]:
        X.append(dataList[0])
        Y.append(dataList[1])
    X1.append(list(X))
    Y1.append(list(Y))


# plotting Data
for i in range(len(X1)):
    plt.plot(X1[i],Y1[i],linespec[i])

# plotting centroid
for i in range(len(centroid)):
     plt.plot([int(centroid[i][0])],[int(centroid[i][1])],'kd')


plt.axis([0,50,0,50]) # setting an axis
plt.show()