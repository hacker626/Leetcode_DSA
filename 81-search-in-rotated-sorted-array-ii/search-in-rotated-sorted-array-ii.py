class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target == nums[mid]:
                return True
            elif nums[start] < nums[mid]:
                if nums[start] <= target and nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:
                if nums[end] >= target and nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1

        return False