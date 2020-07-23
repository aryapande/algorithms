def p(arr):
    c = []
    for x in arr:
        if(x!=None):
            c.append(x)
    print(c)
    
def all_sub(arr,subset,i):
    if(i==len(arr)):
        p(subset)
        return
    else:
        subset[i] = None
        all_sub(arr,subset,i+1)
        subset[i] = arr[i]
        all_sub(arr,subset,i+1)



a = [1,2]
s = [None]*len(a)
i = 0

all_sub(a,s,i)
