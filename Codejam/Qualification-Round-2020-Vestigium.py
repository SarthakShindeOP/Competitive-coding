def duplicate(m):
    if len(m)!=len(set(m)):
        return True
    else:
        return False
t=int(input())
for i in range(1,t+1):
    count=0
    dr=0
    dc=0
    d=[]
    l=[]
    a=int(input())
    matrix=[list(map(int,input().split())) for i in range(a)]
    for j in range(0,a):
        count+=matrix[j][j]
    for k in matrix:
        if duplicate(k):
            dr+=1
        else:
            dr+=0
    for b in range(a):
        for c in range(a):
            d.append(matrix[b][c])
    for s in range(a):
        m=[d[s],d[s+a],d[s+(2*a)]]
        l.append(m)
    for e in l:
        if duplicate(e):
            dc+=1
        else:
            dc+=0
    print('Case #{}: {} {} {}'.format(i,count,dr,dc))

