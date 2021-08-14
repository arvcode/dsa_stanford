#Import math functions
#from math import ceil,floor

def integer_mult(x,y):
    '''
    Function: integer_mult 
    Description: Performs Karatsuba multiplication.
    Input: 2 integers in base 10.
    Output : x*y

    '''
    if x<10 and y<10:
        return x*y

    lenx=len(str(x))
    leny=len(str(y))
    if(lenx>leny):
        n=lenx
    else:
        n=leny
    
    m=n//2 
    
    a=x//(10**m)
    b=x%(10**m)
    
    c=y//(10**m)
    d=y%(10**m)
    
    ac=integer_mult(a,c)
    bd=integer_mult(b,d)
    p=a+b
    q=c+d
    pq=integer_mult(p,q)
    adbc=pq-ac-bd
    
    res=(10**(m*2))*ac+(10**(m))*adbc+bd
    return int(res)

#Test input
res=integer_mult(1234,5678)
print(res)
    
    
#Stanford Algorithms (Coursera) Assignment 1    
num1=3141592653589793238462643383279502884197169399375105820974944592
num2=2718281828459045235360287471352662497757247093699959574966967627
res=integer_mult(num1,num2)
print(res)


