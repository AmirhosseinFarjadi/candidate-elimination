from os import rename, sep
import pandas as pd
import numpy as np
ds=pd.read_csv(r"C:\Users\AmirHossin\Desktop\CandidateElminate\DataSet2.csv")
attribute=np.array(ds)[0:3,:-1]
target=np.array(ds)[0:3,-1]
test_attribute=np.array(ds)[3:6,:-1]
test_target=np.array(ds)[3:6,-1]
print(test_attribute)
attribute_len=len(attribute[0])
#general_hypothesis=[["?"]*attribute_len]*attribute_len
specific_hypothesis=[0]*attribute_len
general_hypothesis=[["?" for i in range(len(specific_hypothesis))] for i in range(len(specific_hypothesis))]
index=[]

def learn (attribute, target):
    for i in range(len(target)):
        if target[i]=="+" and i==0:
            print("Instance is positive")
            specific_hypothesis=attribute[i,:]
            continue
            
        if target[i]=="-":
            print("Instance is negative")
            vector_sample=attribute[i,:]
            for j in range(len(attribute[0])):
                if vector_sample[j]!=specific_hypothesis[j]:
                    general_hypothesis[j][j]=specific_hypothesis[j]
                else:
                    general_hypothesis[j][j]="?"
        if target[i]=="+":
            print("Instance is positive")
            vector_sample=attribute[i,:]
            for k in range(len(attribute[0])):
                if vector_sample[k]!=specific_hypothesis[k]:
                    specific_hypothesis[k]="?"
                    general_hypothesis[k][k]="?"
        print("Specific Hypothesis after ", i+1, "Instance is ", specific_hypothesis)
        print("General Hypothesis after ", i+1, "Instance is ", general_hypothesis)
        print("\n")
    indices = [i for i, val in enumerate(general_hypothesis) if val == ["?", "?", "?", "?", "?"]]
    for s in indices:
        general_hypothesis.remove(["?", "?", "?", "?", "?"])
    return specific_hypothesis, general_hypothesis


specific_final, general_final = learn(attribute,target)
print("Final Specific Hypothesis: ", specific_final, sep="\n")
print("Final General Hypothesis: ", general_final, sep="\n")
print("\n")
for j in range(len(specific_final)):
    if specific_final[j]!='?':
        index.append(j)

farziye=[["japan", "?", "?", "?", "economy"], ["?", "?", "blue", "?", "economy"], ["japan", "?", "blue", "?", "?"]]
print("Gained Hypothesis: ",farziye,sep="\n")
print("\n")
fn=[0,0,0]  #False Negative
fp=[0,0,0]  #False Positive
tn=[0,0,0]  #True Negative
tp=[0,0,0]  #True Positive
Acc=[0,0,0] #Accuracy
for k in range(0, 3):
    for s in range(len(attribute[0])):
        if farziye[k][s]!='?':
            if farziye[k][s]!=test_attribute[k][s] and test_target[k]=="-":
                fn[k]+=1
                break
            elif farziye[k][s]!=test_attribute[k][s] and test_target[k]=="+":
                fp[k]+=1
                break
for k in range(0, 3):
    for s in range(0, 3):
        flag=0
        for t in range(len(attribute[0])):
            if test_attribute[k][t]!='?' and farziye[s][t]==test_attribute[k][t]:
                flag+=1
                if t==4 and flag==2 and test_target[k]=="-":
                    tn[s]+=1
                elif t==4 and flag==2 and test_target[k]=="+":
                    tp[s]+=1
                   
for l in range(0, 3):
    Acc[l]=(tp[l]+tn[l])/(tp[l]+tn[l]+fp[l]+fn[l])
    print("Accuracy of Hypothesis ",l," is: ", Acc[l])
              