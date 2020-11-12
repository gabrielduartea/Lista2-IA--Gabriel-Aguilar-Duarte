import numpy as np 
c=np.zeros((6,6))
a=np.loadtxt('grafo')
b=a
linhas= len(a)
print("  0  1  2  3  4  5\n")

    
for i in range(linhas):
    x=int(a[i][0])
    y=int(a[i][1])
    c[x][y]=1
    

        
print (c)
grau=0
for i in range(6):

    for j in range(6):
        if c[i][j]==1:
            grau=grau+1
           
        if j==5:
                print("vertice:",i,"grau:",grau)
                grau=0