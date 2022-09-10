class Solution:
    def search_pair(self, arr, target_sum, left, triplets):
        right = len(arr) - 1
        while(left < right):
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:  # found the triplet
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1  # skip same element to avoid duplicate triplets
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1  # skip same element to avoid duplicate triplets
            elif target_sum > current_sum:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1  # we need a pair with a smaller sum 
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
                continue
            self.search_pair(arr, -arr[i], i+1, triplets)
        
        
        return triplets


        

                        

            
                        
        