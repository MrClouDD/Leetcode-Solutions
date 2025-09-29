#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        thousand = len(s) - s.find("M") if s.find("M") != -1 else -1
        five_hundred = len(s) - s.find("D") if s.find("D") != -1 else -1
        hundred = len(s) - s.find("C") if s.find("C") != -1 else -1
        fifty = len(s) - s.find("L")  if s.find("L") != -1 else -1
        ten = len(s) - s.find("X")  if s.find("X") != -1 else -1
        five = len(s) - s.find("V") if s.find("V") != -1 else -1
        one = len(s) - s.find("I") if s.find("I") != -1 else -1
        
        print(thousand, five_hundred, hundred, fifty, ten, five, one, sep=",")
        
        # positions = {}
        # letters = ["M", "D", "C", "L", "X", "V", "I"]
        
        # for c in letters:
        #     positions[c] = []
        #     for i, ch in enumerate(s):
        #         if (ch == c):
        #             positions[ch].append(i)
            
        # print(positions, sep=",")
        
        
            
        
        
        
# @lc code=end

