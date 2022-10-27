# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
  l = 0
  r = nums.length-1
  while l<=r
    mid = (l+r).div(2)
    if target > nums[mid]
      l = mid+1
    elsif target < nums[mid]
      r = mid-1
    else
      return mid
    end
  end
  return -1
end

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
puts search([-1,0,3,5,9,12],9)
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
puts search([-1,0,3,5,9,12],2)
# Output: -1
# Explanation: 2 does not exist in nums so return -1