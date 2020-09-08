a = [1,2,0,2,2,2,1,0,0,1]
print(len(a))
h = len(a)-1
l = 0
for x in a:
    if (x==0):
        l+=1
    elif(x==2):
        h-=1
n= [0]*l+[1]*(h-l+1)+[2]*(len(a)-h-1)
print(n)
