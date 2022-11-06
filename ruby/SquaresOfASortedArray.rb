# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 
# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 
# @param {Integer[]} nums
# @return {Integer[]}
def sorted_squares(nums)
  len = nums.length
  result = []
  left = 0
  right = len-1
  (len-1).downto(0).each do |i|
    if nums[left].abs < nums[right].abs
      square = nums[right]
      right-=1
    else 
      square = nums[left]
      left+=1
    end
    result[i] = square * square
  end
  return result
end