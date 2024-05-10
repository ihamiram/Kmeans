import random
from re import L
import numpy as np
import math
K=int(input("please enter a k = "))
A=[]
C=[]
D=[]
while(True):
    distance_choose=int(input("please enter number  from 1)manhatan distance and 2)Euclidean distance"))
    if distance_choose==1 or distance_choose==2:
        break
    else: 
        continue
       
f = open("A:\\points.txt", "r")
A=f.readlines()

for i in range(len(A)):
    A[i] = A[i].rstrip("\n")
    
    
    A[i]=A[i].split(",")    
for i in range(len(A)):
    for j in range(3):
        if A[i][j]=='?' or A[i][j]=='':
            C.append(i)            
for  i in range(len(C)):
    D.append(A[C[i]])
for i in range(len(D)):
     A.remove(D[i])    
for i in range(len(A)):
    for j in range(3):
        A[i][j]=float(A[i][j])       
        
print("clean A =",A)
CENTER=[]
for i in range(K):
    CENTER_POINT=[]
    X1=round(random.uniform(-10, 10),2)  
    X2=round(random.uniform(-10, 10),2)
    X3=round(random.uniform(-10, 10),2)
    CENTER_POINT.append(X1)
    CENTER_POINT.append(X2)
    CENTER_POINT.append(X3)
    CENTER.append(CENTER_POINT)
    
print('RANDOM CENTER= ',CENTER)
if  distance_choose==1:    
    distancee=np.zeros((len(A),K))  
    for i in range(K):
         for j in range(len(A)):
          
           distancee[j][i]= round(((CENTER[i][0]-A[j][0])**2)+((CENTER[i][1]-A[j][1])**2)+((CENTER[i][2]-A[j][2])**2),2)
           
    print('DISTANCE= ',distancee)
    Label=[]
    for i in range(K):
        label1=[]
        Label.append(label1)
    
    min_indexes=[]  
    for row in distancee:
        min_value=min(row)
    
        min_indexes.append(min_value)
    
    print('MIN INDEX = ',min_indexes)
    indexi=[]
    for i in range(len(min_indexes)):
        for j in range(K):
            if min_indexes[i]==distancee[i][j]:
                indexi.append(j)
    for i in range(len(A)):            
        for j in range(K):
    
            if indexi[i]==j:
                Label[j].append(A[i])
         
    print("LABEEEEEEL = ", Label, len(Label))
    count_of_labels=len(Label)

    new_centers=np.zeros((K,3))
    count=[]
    for i in range(count_of_labels):
        count.append(len(Label[i]))
    print(count)
    for m in range(len(count)):
        for i in range(count[m]):
           new_centers[m][0]=Label[m][i][0]+new_centers[m][0]
           new_centers[m][1]=Label[m][i][1]+new_centers[m][1]
           new_centers[m][2]=Label[m][i][1]+new_centers[m][2]
    for m in range(len(count)):
        for i in range(3):
            new_centers[m][i]=new_centers[m][i]/count[m]
            
    print("new_centers = ", new_centers)
    centerr=[]
    centerr.append(CENTER)
    centerr.append(new_centers)
    count_iterate=0
    while(centerr[-1] != centerr[-2]).all():
        count_iterate=count_iterate+1

        new_distancee=np.zeros((len(A),K)) 
        for i in range(K):
            for j in range(len(A)):
          
                new_distancee[j][i]= round(((new_centers[i][0]-A[j][0])**2)+((new_centers[i][1]-A[j][1])**2)+((new_centers[i][2]-A[j][2])**2),2)
    
        Label=[]
        for i in range(K):
            label1=[]
            Label.append(label1)
    
        min_indexes=[]  
        for row in new_distancee:
            min_value=min(row)
    
            min_indexes.append(min_value)
    
        print(min_indexes,len(min_indexes))
        indexi=[]
        for i in range(len(min_indexes)):
            for j in range(K):
                if min_indexes[i]==new_distancee[i][j]:
                    indexi.append(j)
        for i in range(len(A)):            
            for j in range(K):
    
                if indexi[i]==j:
                    Label[j].append(A[i])
         
        print(" LABEL=  ", Label, len(Label))
        count_of_labels=len(Label)
        new_centers=np.zeros((K,3))
        count=[]
        for i in range(count_of_labels):
            count.append(len(Label[i]))
        print("count of label = ", count)
        for m in range(len(count)):
            for i in range(count[m]):
                new_centers[m][0]=Label[m][i][0]+new_centers[m][0]
                new_centers[m][1]=Label[m][i][1]+new_centers[m][1]
                new_centers[m][2]=Label[m][i][1]+new_centers[m][2]
        for m in range(len(count)):
            for i in range(3):
                new_centers[m][i]=new_centers[m][i]/count[m]
            
        print("newcenter= ",new_centers) 
        centerr.append(new_centers)
    
    
    for i in range(len(Label)):
        print("Label","[",i,"] = ",Label[i])
    
    print(new_centers,count_iterate)    
        
elif  distance_choose==2:
    distancee=np.zeros((len(A),K))  
    for i in range(K):
         for j in range(len(A)):
          
           distancee[j][i]= abs((CENTER[i][0]-A[j][0]))+abs((CENTER[i][1]-A[j][1]))+abs((CENTER[i][2]-A[j][2]))
           
    print('DISTANCE= ',distancee)
    Label=[]
    for i in range(K):
        label1=[]
        Label.append(label1)
    
    min_indexes=[]  
    for row in distancee:
        min_value=min(row)
    
        min_indexes.append(min_value)
    
    print('MIN INDEX= ',min_indexes)
    indexi=[]
    for i in range(len(min_indexes)):
        for j in range(K):
            if min_indexes[i]==distancee[i][j]:
                indexi.append(j)
    for i in range(len(A)):            
        for j in range(K):
    
            if indexi[i]==j:
                Label[j].append(A[i])
         
    print("LABEEEEEEL= ", Label, len(Label))
    count_of_labels=len(Label)

    new_centers=np.zeros((K,3))
    count=[]
    for i in range(count_of_labels):
        count.append(len(Label[i]))
    print(count)
    for m in range(len(count)):
        for i in range(count[m]):
           new_centers[m][0]=Label[m][i][0]+new_centers[m][0]
           new_centers[m][1]=Label[m][i][1]+new_centers[m][1]
           new_centers[m][2]=Label[m][i][1]+new_centers[m][2]
    for m in range(len(count)):
        for i in range(3):
            new_centers[m][i]=new_centers[m][i]/count[m]
            
    print(new_centers)
    centerr=[]
    centerr.append(CENTER)
    centerr.append(new_centers)
    count_iterate=0
    while(centerr[-1] != centerr[-2]).all():
        count_iterate=count_iterate+1

        new_distancee=np.zeros((len(A),K)) 
        for i in range(K):
            for j in range(len(A)):
          
                new_distancee[j][i]= abs((new_centers[i][0]-A[j][0]))+abs((new_centers[i][1]-A[j][1]))+abs((new_centers[i][2]-A[j][2]))
    
        Label=[]
        for i in range(K):
            label1=[]
            Label.append(label1)
    
        min_indexes=[]  
        for row in new_distancee:
            min_value=min(row)
    
            min_indexes.append(min_value)
    
        print(min_indexes,len(min_indexes))
        indexi=[]
        for i in range(len(min_indexes)):
            for j in range(K):
                if min_indexes[i]==new_distancee[i][j]:
                    indexi.append(j)
        for i in range(len(A)):            
            for j in range(K):
    
                if indexi[i]==j:
                    Label[j].append(A[i])
         
        print(" LABEL=  ", Label, len(Label))
        count_of_labels=len(Label)
        new_centers=np.zeros((K,3))
        count=[]
        for i in range(count_of_labels):
            count.append(len(Label[i]))
        print("count of label= ", count)
        for m in range(len(count)):
            for i in range(count[m]):
                new_centers[m][0]=Label[m][i][0]+new_centers[m][0]
                new_centers[m][1]=Label[m][i][1]+new_centers[m][1]
                new_centers[m][2]=Label[m][i][1]+new_centers[m][2]
        for m in range(len(count)):
            for i in range(3):
                new_centers[m][i]=new_centers[m][i]/count[m]
            
        print("newcenter= ",new_centers) 
        centerr.append(new_centers)
    
    
    for i in range(len(Label)):
        print("Label","[",i,"] = ",Label[i])
    
    print(new_centers,count_iterate)    
        





 






















