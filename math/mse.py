#n = # of data points
#yi ACTUAL value for the i-th data point
#yi~ = PREDICTED VALUE for the i-th data point

#create function squared errors
#n = number of data points
#yi = ith actual value 
#zip?
#yj= ith predicted value

#create variable error=(yi-yj)

#sum_of = sum(squared erorrs)
#divide sum_of by n

#edge cases
#empty lists
#unequal lists

x = [1, 2, 3, 4]
y = [2, 3, 5, 7]
n = len(x)

def mean_square_error(x,y):
    return sum((i-j)**2 for i, j in zip(x,y))/n

ans= mean_square_error(x,y)

print(f"Mean Square Error = {ans}")