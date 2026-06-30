class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 先排序才知道怎樣移動
        nums.sort()

        # 固定第一個數 a，也就是 nums[i]
        for i in range(len(nums)):
            # 如果 nums[i] > 0 可以直接結束，因為後面也只會更大
            if nums[i] > 0:
                break
            # 去重複的重點是跟過去比，不是跟未來比，不然會出現 [-1,-1,2] 的例子，會錯失答案
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            # 必須是 left < right，因為如果是 left == right，會有指向同樣元素
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1

                elif total < 0:
                    left += 1
                
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 找到答案後才可以對 b, c 去重複，不然會有 [0,0,0,0] 少 [0,0,0] 的答案
                    # 因為提早去重複導致一直跳過 0 的值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 收集完答案也去重複了，可以往下一個值去移動
                    left += 1
                    right -= 1
        return result