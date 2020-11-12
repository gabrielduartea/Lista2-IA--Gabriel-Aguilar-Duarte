import numpy as np
mat = np.array([["1", "2", "3"], ["5", " ", "6"], ["7","4","8"]])    # 2 x 3 array


print("Estado incial:\n",mat,"\n")
print("Estados subsequentes:")
x=mat[0][1]
mat[0][1]=mat[1][1]
mat[1][1]=x
print(mat,"\n")
x=mat[0][1]
mat[0][1]=mat[1][1]
mat[1][1]=mat[1][2]
mat[1][2]=x
print(mat,"\n")
x=mat[1][2]
mat[1][2]=mat[1][1]
mat[1][1]=mat[1][0]
mat[1][0]=x
print(mat,"\n")
x=mat[1][0]
mat[1][0]=mat[1][1]
mat[1][1]=mat[2][1]
mat[2][1]=x
print(mat,"\n")