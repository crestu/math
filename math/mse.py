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

def mean_square_error(x,y):

    n = len(x)
    yi  = None
    yj= None

    error = yi-yj
    me_sum = sum(error)

    ans = me_sum/n

    return ans

ans= mean_square_error()

print(f"Mean Square Error = {ans}")



