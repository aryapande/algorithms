a = 'abchcdctc'
b = 'abccc'
#common sub
arr = [[-1]*(len(b)+1)]*(len(a)+1)
print(len(arr))
def lcs(x,y,p,q):
    
    if(p==0 or q==0):
        arr[p][q] = 0
        return arr[p][q]
    print(p,q)
    if(arr[p][q]!=-1):
        return arr[p][q]
    if(x[p-1]==y[q-1]):
        arr[p][q]=(lcs(x,y,p-1,q-1)+1)
        return arr[p][q]
    else:
        arr[p][q]= max(lcs(x,y,p-1,q),lcs(x,y,p,q-1))
        return arr[p][q]
lcs(a,b,len(a),len(b))
print(arr)
print(arr[len(a)][len(b)])
