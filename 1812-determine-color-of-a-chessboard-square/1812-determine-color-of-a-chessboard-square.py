class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        w_even = ['a', 'c', 'e', 'g']
        
        if coordinates[0] in w_even:
            if int(coordinates[1]) %2 == 0:#even 
                return True
            else:
                return False
        else:
            if int(coordinates[1]) %2 == 0:#even 
                return False
            else:
                return True