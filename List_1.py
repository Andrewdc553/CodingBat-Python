def max_end3(nums):
"""
Given an array of ints length 3, figure out which is larger, 
the first or last element in the array, and set all the other 
elements to be that value. Return the changed array.
max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""
#solution 1:
  if nums[0] >= nums[2]:
    return [nums[0]] * 3
  elif nums[2] >= nums[0]:
    return [nums[2]] * 3

#solution2:
return [nums[0]] * 3 if nums[0] >= nums[2] else [nums[2]] * #



def sum2(nums):
"""
Given an array of ints, return the sum of the first 2 elements in the array.
If the array length is less than 2, just sum up the elements that exist, 
returning 0 if the array is length 0.
sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""
#solution1:
  if len(nums)>= 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0
#solution2:
    return sum(nums[:2])
    
def middle_way(a, b):
"""
Given 2 int arrays, a and b, each length 3, 
return a new array length 2 containing their middle elements.
middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""
  return [a[1], b[1]]

def make_ends(nums):
"""
Given an array of ints, return a new array length 2 containing the 
first and last elements from the original array. The original array will be length 1 or more.
make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
"""
  return [nums[0], nums[-1]]

def has23(nums):
"""
Given an int array length 2, return True if it contains a 2 or a 3.
"""
  return 2 in nums or 3 in nums 
