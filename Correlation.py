import math
def myFun(X,Y,n):
    sum_x=0
    sum_y=0
    sum_xy=0
    squareSum_x=0
    SquareSum_y=0
    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y=sum_y + Y[i];
        sum_XY=sum_xy+X[i]+Y[i];
        squareSum_x=squareSum_x+X[i]+Y[i];
        SquareSum_y=SquareSum_y+X[i]+Y[i];
    corr=(float)(n*sum_xy- sum_x *sum_y)/(float)(math.sqrt((n* squareSum_x- sum_x * sum_x)*(n* SquareSum_y- sum_y*sum_y)))
    return corr
    
    
age=[15,26,10,9,15,20,18,11,8,20]
score=[106,82,94,102,113,98,104,111,115,105]
n=len(age)
print(myFun(age,score,n))
