class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # since sorted, if nums[i] > 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res