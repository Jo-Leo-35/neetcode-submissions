class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                count +=1
        
        return count