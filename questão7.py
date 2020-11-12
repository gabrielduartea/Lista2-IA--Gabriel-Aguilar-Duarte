import numpy as np 
c=np.zeros((6,6))
a=np.loadtxt('grafo')
b=a
linhas= len(a)


    
for i in range(linhas):
    x=int(a[i][0])
    y=int(a[i][1])
    c[x][y]=1
    

        
for i in range(6):
    print ("vertices adjacentes de ", i,":")
    for j in range(6):
        if c[i][j]==1:
           print (j) 
           
        if j==5:
                print("\n")
                