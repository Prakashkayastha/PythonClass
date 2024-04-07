def findGCD(x,y):
    while y:
        x,y=y,x%y
    return x
def findLCM(x,y):
    while y:
        x,y=y,x%y
    return x
def findsq(num):
    start,end=0,num
    mid=(start + end) // 2
    while start <= end:
        if(mid * mid == num):
          print(f"The square root of the {num} is {mid} ")
          break
        elif (mid*mid > num):
            end = mid-1
        else:
            start = mid+1
        mid=(start + end) // 2

def swap(a,b):
    print(f"Before swap: a={a} and b={b}")
    a=a^b
    b=a^b
    a=a^b
    print(f"After swap a={a} and b={b}")