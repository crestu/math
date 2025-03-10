#y = a +bx
#a = [(Ey)(Ex**2)-(Ex)(Exy)]/[n(Ex**2)-(Ex)**2]
#b= [n(Exy)-(Ex)(Ey)]/[n(Ex**2)-(Ex)**2]
#n = # of data points
#define x
#define y
#calculate Ex
#calculate Ey
#function to calculate Ex**2
#function to calculate Exy
# create linear regression function

x = [3, 9, 5, 3]
y = [8, 6, 4, 2]
n = len(x)

def Ex_squared(x):
    return sum(i**2 for i in x)

def Exy(x, y):
    return sum(i * j for i, j in zip(x, y))
            
def linear_regression(x, y):
    Ex = sum(x)
    Ey = sum(y)
    
    a = ((Ey * Ex_squared(x)) - (Ex * Exy(x, y))) / ((n * Ex_squared(x)) - Ex**2)
    b = ((n * Exy(x, y)) - (Ex * Ey)) / ((n * Ex_squared(x)) - Ex**2)

    return a, b

a, b = linear_regression(x, y)

print(f"y = {a:.2f} + {b:.2f}x")