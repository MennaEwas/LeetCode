class Solution:
    def numberOfSteps(self, num: int) -> int:
        step =  0
        while num:
            if num%2 == 0: #even 
                num /= 2
            else:
                num -= 1
            step += 1
            
        return step 