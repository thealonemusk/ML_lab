import pandas as pd
import math as m
df = pd.read_csv("Points.csv")
x = []
y = []
for _, row in df.iterrows():
    x.append(row['x'])
    y.append(row['y'])

data = list(zip(x, y))
k = 2

def distance(p1, p2):
    temp = m.pow((p2[1] - p1[1]), 2) + m.pow((p2[0] - p1[0]), 2)
    dis = m.sqrt(temp)
    return dis

def minDistIndex(dist):
    index = 0
    min = dist[0]
    for i in range(len(dist)):
        if dist[i] < min:
            min = dist[i]
            index = i
    return index

def assignClusters(data, centroids):
    clusters = dict()
    for i in range(k):
        clusters[i] = list()

    for i in range(len(data)):
        dist = list()
        for j in range(len(centroids)):
            dist.append(distance(centroids[j], data[i]))
        clusters[minDistIndex(dist)].append(data[i])
    return clusters

def calcNewCentroids(clusters):
    newCentroids = list()
    for key in clusters.keys():
        x = 0.0
        y = 0.0
        for p in clusters[key]:
            x = x + p[0]
            y = y + p[1]
        x = x / len(clusters[key])
        y = y / len(clusters[key])

        pt = (x, y)
        newCentroids.append(pt)
    return newCentroids
   
def kMeans(data, k):
    centroids = list()
    for i in range(k):
        centroids.append(data[i])
    
    clusters = dict()

    isSame = 0
    while(isSame == 0):
        clusters = assignClusters(data, centroids)
        newCentroids = calcNewCentroids(clusters)

        isSame = 1
        for i in range(k):
            if centroids[i] != newCentroids[i]:
                isSame = 0

        for i in range(k):
            centroids[i] = newCentroids[i]
    
    for key in clusters.keys():
        print(f"\n\nCluster No. {key} => Centroid : {centroids[key]}\nPoint in the Cluster : ")
        for p in clusters[key]:
            print(p, end=", ")

kMeans(data, k)