# importing NumPy Library
import numpy as np
import sys

# Reading number of unknown variable
n = int(input("Enter number of unknown variables to Find: "))
col = [] # defining one empty array as col

for i in range(0, n): # From the range of 0 to n number.
    row = [] # Assigning or defining another empty array as row

    # Making a range from 0 to n+1 size because one extra column 
    # for 'B' value when making into Augmented matrix 
    for j in range(0, n+1): 
        # Making the user to give input of the matrix according to its index
        print('Enter the value in ['+str(i)+']['+str(j)+'] = ',end=' ')
        temp = float(input()) # this code shows or accept both floating point number that store in temp 
        row.append(temp) # appending the given value as array in row that we
        print(row) 
    col.append(row) # the value inserted into the row[] is appending to col[]

A = np.matrix(col) # Assigning matrix to A using matrix function in the numpy
print('\n')
print('The Augmented matrix is: \n',A) # Printing the matrix in Augmented form

print('\n')

# Logic
for i in range (0, n): # For a given n matrix.
    # If the pivot element happens to be 0, then 
    if col[i][i] == 0.0: 
        print("Swap rows, you can't have zero in diagonal Matrix. \nTry Again!")
        sys.exit() # call sys library to exit from the code execution

    for j in range(0, n):
        # assigning pivot element to piv
        # Starting from first row till the end of the column, 
        # it is dividing by pivot element
        A[i,:] = A[i,:]/A[i,i]

        # When i != j, which means for non-pivot element
        if i != j:
            # I have assigned that non-pivot element to factor 
            # after dividing it by pivot element
            factor = A[j,i]/A[i,i]
            # in column side, I have n+1 size including the 'B' value forming Augmented Matrix
            for k in range(0, n+1):
                A[j,k] = A[j,k] - factor*A[i,k]

print('The Matrix A after doing Gauss Jordan method is: \n',A)
print('\n')
print('And the value of unknown variable is: \n',A[:,n])
