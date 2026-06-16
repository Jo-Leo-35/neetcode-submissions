class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement not in hashMap:
                hashMap[nums[i]] = i
            else:
                index = hashMap[complement]
                return [index, i]
