a = [1,5,6,8,9,45]
b=[-2,-1,3,4,6,9,10]
c = []
i = 0
j = 0
k=0
while(i<(len(a)-1) and j<(len(b)-1)):
    if(a[i]<=b[j]):
        c.append(a[i])
        i+=1
        print('i:',i)

    elif(a[i]>b[j]):
        c.append(b[j])
        j+=1
        print('j:',j)

if(i==(len(a)-1)):
    for x in range(j,len(b)-1):
        c.append(b[x])
elif(j==(len(b)-1)):
    for x in range(i,len(a)-1):
        c.append(a[x])
print(c)
