st = [200,400,500]
final_destination = 800
st.append(final_destination)
m = 1200

v = []

dist = 0
if(st[0]>m):
    print('imp')
i = 0
x=-1
for x in range(len(st)-1):
    a = st[x]-(i+m)
    b = st[x+1]-(i+m)
    if(a<=0 and b>0):
        i = st[x]
        v.append(i)
        print(x)
    if(a>0):
        print('not poss')
if((st[x+1]-(i+m))>0):
    print('ending broken')
    v = []
print(v)
