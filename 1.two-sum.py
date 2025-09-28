#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = target - nums[i]
            for j in range(len(nums)):
                if nums[j] == temp and i != j:
                    ans = [i, j]
                
        return ans
# @lc code=end

