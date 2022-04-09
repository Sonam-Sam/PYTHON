# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknown variable
n = int(input('Enter number of unknown variables to Find: '))

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix that is one column for 'B' value.
a = np.zeros((n, n))
b = np.zeros(n)

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('***Enter the Matrix coefficient in the form of Augmented Matrix***')

for k in range(n):
    for j in range(n):
        a[i][j] = float(input( 'The value in ['+str(i)+']['+str(j)+'] = '))

    for l in range(n):
        b[n][j] = float(input( 'The value of b ['+str(n)+']['+str(j)+'] = '))

    # Partial pivoting
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range (k+1, n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k,n):
                        a[k,j],a[i,j] = a[i,j],a[k,j]
                    b[k],b[i] = b[i],b[k]
                    break
        # Division of the pivot row
        pivot = a[k,k]
        for j in range(k,n):
            a[k,j] /= pivot
        b[k] /= pivot
        
        #Elimination loop
        for i in range(n):
            if i == k or a[i,k] == 0:
                continue
            factor = a[i,k]
            for j in range(k,n):
                a[i,j] -= factor * a[k,j]
            b[i] -= factor * b[k]

# Obtaining the metrix that you have entered in the form of Augmented Matrix
print(a)

# Displaying solution
print('\nSolution [a] is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')