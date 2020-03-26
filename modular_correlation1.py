import math
a=[15,26,10,9,15,20,18,11,8,20]
b = [106,82,94,102,113,98,104,111,115,105]
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
print ("Mental Ability Prediction")
print(correlation(a,b))