class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create an empty dictionary to store numbers we've seen: {number: index}
        seen = {}
        
        # Loop through the list, tracking both the index (i) and the value (num)
        for i, num in enumerate(nums):
            # Calculate what number we need to reach the target
            complement = target - num
            
            # If that needed number is already in our dictionary, we found a match!
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, save the current number and its index to the dictionary
            seen[num] = i