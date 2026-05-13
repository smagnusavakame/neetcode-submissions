class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """# Understand 

        I - input is an interger array nums eg [3,5,7,6]



        0 - boolean to return true - when? if any value in this array appears more than once 
                       return false - if all values are disticnt


        C - lenggth of nymber is between  


        E - empty array,

        # Match 
        #for duplicates you would want to definitely stick to mostly usng sets, and that set should be able to tell 
        us if there is no duplicate, we could also use a dictionary


        #Plan 
        1. create an empty set.   [ 1,2,3, ].         [1, 3, 1]
        2. loop through the array.    [ 1, 2, 3, 3]   [1, 3, 1]
        3. append to set
        4;. if length of the set is less than length of the array, then we go ahead and return true, else return false

        """
        #Implement
        seen = set()
        for number in nums:
            seen.add(number)
        if len(seen) < len(nums):
            return True
        else:
            return False


        #Review



        #Evaluate