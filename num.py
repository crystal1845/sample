import numpy as np

list=np.array([45, 36, 10, 68, 20])
print("List: ", list)
print("Shape: ", np.shape)
print("type: ", np.dtype)

#vectoization
new_list=list+5
print("\nList + 5: ", new_list)

#boolean masking
masked_list=new_list[new_list>30]
print("\nMasked list: ", masked_list)

#Broadcasting
cells=np.array([[100, 150, 200], [300, 250, 400]])
bonus=np.array([10, 20, 30])
result=cells+bonus
print("\nCells: ",cells,"\nBonus: ",bonus,"\nResult:",result)

#reshape
reshaped=cells.reshape([3,2])
print("\nReshaped: ", reshaped)

#flatten
flat=list.flatten()
print("\nFlat: ", flat)

#Axis
print("\nSum of axis 0: ", cells.sum(axis=0))
print("\nSum of axis 1: ", cells.sum(axis=1))
print("\nSum of cells: ", cells.sum())

#transpose
tra=cells.transpose()
print("\nTranspose: ", tra)