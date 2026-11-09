class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """# Understand 

        I - input is an interger array nums eg [3,5,7,6]



        0 - boolean to return true - when? if any value in this array appears more than once 
                       return false - if all values are disticnt


        C - lenggth of nymber is between  


        E - empty array

        #Review



        #Evaluate

        """
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
