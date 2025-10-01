import numpy as np

nums = np.arange(1, 11)   
print("Original Array:", nums)


print("Total Sum:", nums.sum())
print("Average Value:", nums.mean())
print("Squares:", np.power(nums, 2))


rand_mat = np.random.random((3, 3))
print("Random Matrix (3x3):")
