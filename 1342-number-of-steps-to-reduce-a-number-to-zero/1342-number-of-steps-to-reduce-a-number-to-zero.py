class Solution:
    def numberOfSteps(self, num: int) -> int:
        step =  0
        while num:
            if not num%2 :
                num /= 2
            else:
                num -= 1
            step += 1
            
        return step 