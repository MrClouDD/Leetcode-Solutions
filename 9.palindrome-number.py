#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        value = True
        for i in range(math.floor(len(s)/2)):
            if (s[i] != s[len(s) - i - 1]):
                value = False
        return value
            
# @lc code=end

