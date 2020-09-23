test_w = [25,50,30,70]
test_v = [70,100,120,10]
w = 70
arr = [[-1]*(len(test_v)+1)]*(w+1)


def knapsack(test_v,test_w,w,n):
    
    if(w == 0 or n==-1):
        return 0
    
    if(arr[w][n]!=-1):
        return arr[w][n]
    
    if(test_w[n]<=w):
        arr[w][n] = max(test_v[n] + knapsack(test_v,test_w,w-test_w[n],n-1),knapsack(test_v,test_w,w,n-1))
        return arr[w][n]
    else:
        arr[w][n] = knapsack(test_v,test_w,w,n-1)
        return arr[w][n]
        
a = knapsack(test_v,test_w,w,len(test_v)-1)
print(a)
