

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
    
"""

#given an array called nums, if there exists a duplicate number in the array return true, else return false


 #Brute force method - exceeds time complexity O(n^2)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
    

#need to lower time complexity, could use a pointers 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l, r = 0, 1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[l] == nums[r]:
                return True
            l += 1
            r += 1 
        return False
#This passes ! tho it could be faster using a hashset    

#need to look into hashsets seems to be the best bet to solve time complexity issue


        