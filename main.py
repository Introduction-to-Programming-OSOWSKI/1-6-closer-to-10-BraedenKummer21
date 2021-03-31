#WRITE YOUR CODE IN THIS FILE
def close10(x,y):

    if abs(x-10) < abs(y-10):
        return x

    elif abs(x-10) > abs(y-10):
        return y 

    else: 
        print("0")

print(close10(5,13))