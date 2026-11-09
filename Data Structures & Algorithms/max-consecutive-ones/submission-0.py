class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        UNDERSTAND THE PROBLEM

        INPUT :
        input is a list of numbers called nums containing binary digits
        return the maximum number of consecutive ones in the array
        




        OUTPUT 
        number of consecutive ones in the array



        CONSTRAINTS
        num is either 0 or 1



        EDGE CASES"""

        max_cnt = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                if current > max_cnt:
                    max_cnt = current
            else:
                current = 0
        
        return max_cnt