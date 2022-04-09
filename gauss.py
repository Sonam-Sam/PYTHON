# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknown variable
n = int(input('Enter number of unknown variables to Find: '))

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix that is one column for 'B' value.
a = np.zeros((n, n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('***Enter the Matrix coefficient in the form of Augmented Matrix***')
print('\n')

for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'The value in ['+str(i)+']['+str(j)+'] = '))

# Applying Gauss Jordan Method
for i in range(n):
    if a[i][i] == 0.0:
        print("Swap rows, you can't have zero in diagonal Matrix. \n Try Again")
        sys.exit()
            
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Obtaining Solution
for i in range(n):
    x[i] = a[i][n]/a[i][i]

# Obtaining the metrix that you have entered in the form of Augmented Matrix
print(a)

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')