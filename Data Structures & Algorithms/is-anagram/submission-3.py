class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Understand 
        """Input :
           given two strings, s and t,

           Ouput :
            return true , when? if these two strings are anagrams of each other, 
            what is an anagram, string that contains the exact same characters as another string

           Constraints: 

           s and t are lowercase letters, we dont need to worry about reducing it to lower case letters. 
        

           Edge Cases:
           s and t are empty, s and t are off differnt lengths, or s and t are both
        



        #Match 

        two pointers, just basic comparison and looping



        #Plan 
        racecar,   carrace 
        that they are the same characters , so basically when we sort both of them, we should get the same thing
        jar ,  jam , ajr, ajm


        """
        #Implement 
        list1 = []
        list2 = []   
        for ch in s:
            list1.append(ch)
        for ch in t:
            list2.append(ch)

        if sorted(list1) == sorted(list2):
            return True
        else:
            return False


        #Review 


        #Evaluate
        