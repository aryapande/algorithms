arr = [3,6,7,4,8]
s = 22
def summation(arr,n,s):
    print(s,n)
    if(s == 0):
        return True
    if(n==0):
        return False
    
    if(arr[n-1]>s):
        return summation(arr,n-1,s)
    else:
        return (summation(arr,n-1,s-arr[n-1]) or summation(arr,n-1,s))

f = summation(arr,len(arr),s)
print(f)
