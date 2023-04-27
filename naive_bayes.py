import pandas as pd
import numpy as np

df = pd.read_csv("NaiveBayes.csv")
today={'Outlook':'Sunny','Temperature':'Cool',"Humidity":'Normal','Windy':'True'}
targetAttr = 'PlayGolf'

noOfClasses = np.unique(df[targetAttr])

def currentProb(subdataset, new):
    prob = 1.0
    for key, value in new.items():
        p = 0.0
        n = 0.0
        for _, row in subdataset.iterrows():
            if row[key] == value:
                p = p + 1
            else:
                n = n + 1
        prob = prob * (p/(p + n))
    return prob

def priorProb(dataset, noOfClasses):
    probOfClasses = []
    for cls in noOfClasses:
        subdataset = dataset[dataset[targetAttr] == cls]
        prob = currentProb(subdataset, today) * float(len(subdataset)) / float(len(dataset))
        probOfClasses.append(prob)
    return probOfClasses

def max(probs):
    mx = 0
    for i in range(len(probs)):
        if probs[i] > probs[mx]:
            mx = i
    return mx

probs = priorProb(df, noOfClasses)
clsIndex = max(probs)

print(f"\nNew Example : {today}")
print(f"\nClass It belongs to : {noOfClasses[clsIndex]}\n")