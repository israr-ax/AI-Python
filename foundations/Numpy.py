import numpy as np 
arr = np.array([1,2,3,4,5])
type(arr)
print(arr)

matrix=np.array([[2,3,4,5],
                 [5,2,3,1]])
print(matrix)
print(f"Dimensions: {matrix.shape}")
print(f"Numberof Dimnsions: {matrix.ndim}")
print(f"Total elements: {matrix.size}")
print(f"Data Type: {matrix.dtype}")



Sum=np.sum(arr)
print(f"total Sum of array {arr}: {Sum}")
MEAN = np.mean(arr)
print(f"Meanof array {arr}: {MEAN}")


''' Small Coding Task

# Create a program that:
# Takes a list of 5 numbers
# Converts it to NumPy array Prints: Sum Mean Maximum '''

con=[]
for i in range(5):
    numm=int(input(f"Enter {i} nummber: "))
    con.append(numm)
print(con)
arr=np.array(con)
print(type(con))
print(type(arr))

print(f"Sum of list:{np.sum(arr)}\nMean of list: {np.mean(arr)}\nMaximum of List: {np.max(arr)}")

'''  _________________________________________
    |Topic 2: Indexing & Slicing in NumPy     |
    |_________________________________________|'''
# Create array [5,10,15,20,25]
# Print second element
Narr=np.array([5,10,15,20,25])
print(f"{Narr}\nPrint second element: {Narr[1]}")

# Print last three elements
print(f"Print last three elements: {Narr[-3:]}")

# Print every second element
print(f"Print every second element: {Narr[0:5:2]}")


arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])

# Get middle element Get first two rows & last two column

print(f"Get Center element: {arr[1,1]}")
print(f"Get first two rows & last two column:{arr[0:2,1:3]} ")
print(f"Get first Row:{arr[0]} ")
print(f"Get Second Column:{arr[:,1]} ")

'''  _________________________________________
    |Topic 3: NumPy Operations & Broadcasting |
    |_________________________________________|'''
 

# Create array [1,2,3], Add 5 to it
arr = np.array([[10,20,30]])
print(arr+5)

# Multiply [2,4,6] with [1,2,3]print(arr+5)
arr = np.array([[2,4,6]])
arr2=np.array([2,4,6])
print(arr * arr2)


# Write a program:Create array [10,20,30,40],Multiply by 2,Find sum & mean

arr=np.array([10,20,30,40])
print(f"{arr} \nMultiply by 2. :{arr * 2} \nTotal Sum of an array:{np.sum(arr)} \nMean of an array: {np.mean(arr)} ")

'''  _________________________________________________
    | Topic 4: Reshaping, Stacking & Splitting Arrays |
    |_________________________________________________|'''
    

# Reshape [1,2,3,4] into 2x2
arr=np.array([1,2,3,4])
new_arr=arr.reshape(2,2)
print(f"Before Reshape: {arr} \nAfter Reshape: {new_arr}")

# Stack [1,2] and [3,4] vertically and Horizantally
a=np.array([1,2])
b=np.array([3,4])
print(f"Vertical Stack: {np.vstack((a,b))} \nHorizantal Stack: {np.hstack((a,b))}")


# Split [10,20,30,40] into 2 parts
arr=np.array([10,20,30,40])
print(np.split(arr,2))



 
