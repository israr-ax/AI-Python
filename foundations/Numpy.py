import numpy as np 
# arr = np.array([1,2,3,4,5])
# type(arr)
# print(arr)

# matrix=np.array([[2,3,4,5],
#                  [5,2,3,1]])
# print(matrix)
# print(f"Dimensions: {matrix.shape}")
# print(f"Numberof Dimnsions: {matrix.ndim}")
# print(f"Total elements: {matrix.size}")
# print(f"Data Type: {matrix.dtype}")



# Sum=np.sum(arr)
# print(f"total Sum of array {arr}: {Sum}")
# MEAN = np.mean(arr)
# print(f"Meanof array {arr}: {MEAN}")


# ''' Small Coding Task

# Create a program that:
# Takes a list of 5 numbers
# Converts it to NumPy array Prints: Sum Mean Maximum '''

# con=[]
# for i in range(5):
#     numm=int(input(f"Enter {i} nummber: "))
#     con.append(numm)
# print(con)
# arr=np.array(con)
# print(type(con))
# print(type(arr))

# print(f"Sum of list:{np.sum(arr)}\nMean of list: {np.mean(arr)}\nMaximum of List: {np.max(arr)}")


# Topic 2: Indexing & Slicing in NumPy

# Create array [5,10,15,20,25]
# Print second element

Narr=np.array([5,10,15,20,25])
print(f"{Narr}\nPrint second element: {Narr[1]}")

# Print last three elements

print(f"Print last three elements: {Narr[-3:]}")

# Print every second element
