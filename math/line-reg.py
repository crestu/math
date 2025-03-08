#y = a +bx
#a = [(Ey)(Ex**2)-(Ex)(Exy)]/[n(Ex**2)-(Ex)**2]
#b= [n(Exy)-(Ex)(Ey)]/[n(Ex**2)-(Ex)**2]
#n = # of data points
#define x
#define y
#calculate Ex
#calculate Ey

x=[3,9,5,3]
y=[8,6,4,2]
n = len(x)

Ex = sum(x)  
Ey= sum(y)

#function to calculate Ex**2
def Exq(x):
    return sum(i**2 for i in x)

#function to calculate Exy
def Exy(x,y):
    return sum(i*j for i,j in zip(x,y))
            
# create linear regression function
def line_reg(x,y):
    a = ((Ey)*(Exq(x)) - (Ex)*(Exy(x, y))) / ((n * Exq(x)) - (Ex)**2)
    b = ((n * Exy(x, y)) - (Ex * Ey)) / ((n * Exq(x)) - (Ex)**2)

    ans = a+b
    return ans
result = line_reg(x, y)

print(result)
