a = "abcdergerg"
f = False
#https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

for x in range(len(a)):
    if(f==True):
        break
    start = x
    stop = len(a)-1
    cap = len(a)
    for y in reversed(a):
        cap-=1
        if(y == a[start] and x<cap):
            
            stop = cap
            break
        else:
            continue
    if(a[x]!=a[stop]):
        continue
    orig_start = start
    orig_stop = stop
    print(start,stop)
    while(a[start]==a[stop]):
        if(start==stop or start>stop):
            print(a[orig_start:orig_stop+1])
            f = True
            break
        start+=1
        stop-=1
