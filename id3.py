import pandas as pd
import numpy as np
import math as m

attrList = ["outlook", "temp", "humidity", "wind"]

df = pd.read_csv("ID3DT.csv")
class Node:
    def __init__(self):
        self.children = []
        self.value = ""
        self.isLeaf = False
        self.pred = ""

def entropy(dataset):
    pos = 0.0
    neg = 0.0

    for _, row in dataset.iterrows():
        if row["play"] == "Yes":
            pos = pos + 1
        else:
            neg = neg + 1

    if pos == 0.0 or neg == 0.0:
        return 0.0
    else:
        p = pos / (pos + neg)
        n = neg / (pos + neg)
        return -(p * m.log(p, 2) + n * m.log(n, 2))

def infoGain(dataset, attr):
    values_attr = np.unique(dataset[attr])
    gain = entropy(dataset)
    for value in values_attr:
        subdataset = dataset[dataset[attr] == value]
        subEntr = entropy(subdataset)
        gain = gain - (float(len(subdataset)) / float(len(dataset))) * subEntr
    return gain

def ID3(dataset, attrs):
    root = Node()
    max_gain = 0

    for attr in attrs:
        gain = infoGain(dataset, attr)
        if gain > max_gain:
            max_gain = gain
            max_feat = attr
    root.value = max_feat

    maxFeatValues = np.unique(dataset[max_feat])
    for value in maxFeatValues:
        subdataset = dataset[dataset[max_feat] == value]

        if entropy(subdataset) == 0.0:
            newNode = Node()
            newNode.isLeaf = True
            newNode.value = value
            newNode.pred = np.unique(subdataset["play"])
            root.children.append(newNode)

        else:
            dummyNode = Node()
            dummyNode.value = value
            new_attrs = attrs.copy()
            new_attrs.remove(max_feat)
            child = ID3(subdataset, new_attrs)
            dummyNode.children.append(child)
            root.children.append(dummyNode)
    
    return root

def printTree(root: Node, depth=0):
    for i in range(depth):
        print("\t", end="")
    print(root.value, end="")
    if root.isLeaf:
        print(" -> ", root.pred)
    print()
    for child in root.children:
        printTree(child, depth + 1)

def classify(root: Node, new):
    for child in root.children:
        if child.value == new[root.value]:
            if child.isLeaf:
                print("Predicted Label for new example", new," is:", child.pred)
                exit()
            else:
                classify (child.children[0], new)

root = ID3(df, attrList)
print("Decision Tree is:")
printTree(root)
print("------------------\n")

new = {"outlook":"Sunny", "temp":"Hot", "humidity":"Normal", "wind":"Strong"}
classify(root, new)