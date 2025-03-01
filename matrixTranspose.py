a=[[1,2],
   [3,4],
   [5,6]]
trans=[[0,0,0],
   [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        trans[j][i]=a[i][j]
for i in trans:
    print(i)        

