class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = [1] * len(nums)
        right_array = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, len(nums)):# 邊界條件設的非常不好
            left_array[i] = left_array[i-1] * nums[i-1]

        for j in range(len(nums)-2 ,-1, -1):# 邊界條件設的非常不好
            right_array[j] = right_array[j+1] * nums[j+1]

        for k in range(0, len(nums)):
            res[k] = left_array[k] * right_array[k]

        return res

