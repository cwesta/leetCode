"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
    
    
Base Cases:
    if the len of the arr == 1: return the element in the array
    
    find the sum of the overall array
    
    next find the sub array within the array that has a sum larger than the sum of the overall array
    
    if there exists none return the sum of the array
    
    set max_sum = 0 to start 
    
    [-2,1,-3,4,-1,2,1,-5,4]
     ^
    sub_sum = sum([-2, 1, -3, 4])
    
    if sub_sum > max_sum and sub_sum > nums_sum:
        then set max_sum = sub_sum
        
    else continue loop
    
       
    [-2,1,-3,4,-1,2,1,-5,4]
        ^
        sub_sum = sum([1,-3,4,-1])
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        nums_sum = sum(nums)
        max_sum = 0
        

        for i in range(0, len(nums) - 4):
            sub_nums = nums[i:i+4]
            
            if sub_nums > max_sum and sub_nums > nums_sum:
                max_sum = sub_nums
            
        return max_sum
        