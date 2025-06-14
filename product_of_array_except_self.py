# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums 
except nums[i]
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation. 

nums = [1,2,3,4]

# Suffix array 
suffix_array = [1] * len(nums)

# Prefix array 
prefix_arr = [1] * len(nums)
prefix = 1 

for i in range(len(nums)):
  prefix_arr[i] = prefix 
  prefix *= nums[i] 

suffix_arr = [1] * len(nums)
suffix = 1 

for j in range(len(nums)-1, -1, -1):
  suffix_arr[j] = suffix 
  suffix *= nums[j] 

for i in range(len(suffix_arr)):
  suffix_arr[i] *= prefix_arr[i] 

return suffix_arr
