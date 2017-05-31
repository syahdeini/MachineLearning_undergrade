# K-Nearest Neighbors Algorithm
# By. Aldy syahdeini                31-March-2014
#
# 1. find all ED for each data in dataTest to all data in dataTrain
# 2. find K-data which is close to data of dataTest which is being assesed 
# 3. count the frequency of each K-data, 
# 4. decide which class of data based of the highest frequency of K-data  


from cmath import sqrt
from math import pow
import csv
from collections import OrderedDict

def csv_reader(file_obj):
    reader=csv.reader(file_obj,dialect=csv.excel_tab)
    data=[]
    for row in reader:
        data.append(row[0].split(','))
    return data

# Read the data from the dataTrain file file and return the dictionary
def read_data(path):
    #get variables
    with open(path,"rU") as f_obj:
        dataSet=csv_reader(f_obj)
    return dataSet[0],dataSet[1:]       # return variable and data

def getKelas(dataSet):
    kelas=list()
    for data in dataSet:
        kelas.append(data[-1])
    return kelas

# eucledian distance function
def ed(data1,data2):
    sum=0
    for i in range(len(data1)-1):
        sum+=pow(float(data1[i])-float(data2[i]),2)
    return abs(sqrt(sum))

# od_dic{ ed: kelas}
# return the class based on potting
def potting(K,od_Dict):
    kelas_dict=dict()           # for saving a temporary class and frequency
    i=1
    for key in od_Dict:
        i+=1
        if(i>K):
            break
        if od_Dict[key] in kelas_dict.keys():   # check if class is already in kelas_dict
            kelas_dict[od_Dict[key]]+=1          # update frequency apperance class
        else:
            kelas_dict.update({od_Dict[key]:1}) # if class not saved yet, make new element
    # sorted class by value/frequency
    win_list=sorted(kelas_dict,key=kelas_dict.get) #get which class is the most frequncy come out
    return win_list[0]



# read data
var,dataTrain=read_data("dataTrainSimple.csv") # We use variables to avoid "class" when finding ED
kelas=getKelas(dataTrain)
var,dataTest=read_data("dataTestSimple.csv")
print kelas

K=raw_input("inputkan K : ")
# od_dict contains { eucled dist : class } which will be sorted base on minimum of eucledian distance
for i,data1 in enumerate(dataTest):
    ed_dict=dict()
    for idx,data2 in enumerate(dataTrain):
         ed_temp=ed(data1,data2)
         ed_dict.update({ed_temp:kelas[idx]})
    od_dict=OrderedDict(sorted(ed_dict.items()))
    print i,' ',potting(K,od_dict)


