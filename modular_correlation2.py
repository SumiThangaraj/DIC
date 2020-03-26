import math
a=[2,2,1,3,4,1,5,3,1,2]
b=[21,41,23,35,51,22,67,51,19,25]
def mean(x):
    sum = 0.0
    for i in x:
         sum += i
    return sum / len(x) 
    
def StandardDeviation(x):
    sumv = 0.0
    for i in x:
         sumv += (i - mean(x))**2
    return math.sqrt(sumv/(len(x)-1))

def correlation(x, y):
    scorex = []
    scorey = []
    for i in x: 
        scorex.append((i - mean(x))/StandardDeviation(x)) 
    for j in y:
        scorey.append((j - mean(y))/StandardDeviation(y))   
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)
print ("Stumps and Beetle larvae")
print(correlation(a,b))