"""
    Multilayer regression               20-April-2014

"""

import numpy as nm
import math
__author__ = 'syahdeini'


# opening input file
file_obj=open("data.txt","r")
raw_list=file_obj.readlines()
file_obj.close()

# making matrix of data
new_matrix=list()
for raw in raw_list:
    one_row=raw.split(' ')
    # for converting a string value into integer
    temp_list=list()
    for one_val in one_row:
        temp_list.append(int(one_val))
    new_matrix.append(temp_list)

#getting standart deviation matrix
std_mat=nm.matrix(new_matrix).std(0,ddof=1)
#getting mean matrix
temp_mean_mat=nm.matrix(new_matrix).mean(0)
#typecast to list
mean_mat=list()
for i in range(temp_mean_mat.shape[1]):
    mean_mat.append(temp_mean_mat.item(i))


#getting coveriance matry
# tranpose is needed due the correlation of row (row is variable) in corrcoef
data_matrix=nm.matrix(new_matrix).T # making matrix in numpy
cov_matrix=nm.corrcoef(data_matrix)


#getting rii and yi matrix
rii_matrix=nm.matrix(cov_matrix[0:3,0:3])
yii_matrix=nm.matrix(cov_matrix[3:,:3])

# getting matrix inverse of rii
inv_rii_mat=rii_matrix.I
# geting beta
beta_mat=nm.dot(inv_rii_mat,yii_matrix.T)

#getting weight
mat_len=std_mat.shape[1];
divided_std_mat=list()
for val in range(mat_len-1):
#    print std_mat.item(val)
    divided_std_mat.append(std_mat.item(val)/std_mat.item(mat_len-1))

weight_mat=list()
for i,val in enumerate(divided_std_mat):
     weight_mat.append(beta_mat.item(i)/val)

#getting A
temp=0
for i in range(len(weight_mat)):
    temp+=weight_mat[i]*mean_mat[i]
a_weight=mean_mat[-1]-temp

#print persamaan
print 'y= ',round(a_weight,2),
for idx,data in enumerate(weight_mat):
    print '+',round(data,3),'*X[',idx,']',

"""
print data_matrix
print '\n'
print cov_matrix
print '\n'
"""
"""
print inv_rii_mat.shape
print '\n'
print yii_matrix.T.shape
print '\n'
"""

#data=[[1,2,]

