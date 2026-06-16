class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            return k
            


# [0, 1, 1, 1, 2, 3] val = 1
# i = 0, k = 0, nums[0] != 1, nums[0] = nums[0], k = 1
# i = 1, k = 1, nums[1] == 1, continue
# i = 2, k = 1, nums[2] == 2, continue
# i = 3, k = 1, nums[3] == 3, continue
# i = 4, k = 1, nums[4] != 1, num[1] <- nums[4]= 2, k = 2
# i = 5, k = 2, nums[5] != 2, nums[2] <- nums[5] = 3

