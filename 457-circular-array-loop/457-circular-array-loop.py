class Solution:
    def find_index(self, arr, is_forward, current_index):
        direction = arr[current_index]>= 0
        if is_forward != direction:
            return -1 
        next_index = (current_index + arr[current_index]) % len(arr)
        if next_index == current_index:
            next_index = -1

        return next_index
        
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            is_forward = nums[i] >= 0
            slow, fast = i, i
            while True:
                slow = self.find_index(nums, is_forward, slow)
                fast = self.find_index(nums, is_forward, fast)
                if fast != -1:
                    fast = self.find_index(nums, is_forward, fast)
                if fast == -1 or slow == fast or slow == -1:
                    break 
            if fast == slow and slow != -1:
                return True 
        return False
    
                    