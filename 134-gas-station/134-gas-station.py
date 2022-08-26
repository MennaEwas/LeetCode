class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remaining, prev_remianing, candidate = 0, 0, 0
        for i in range(len(gas)):
            remaining += gas[i] - cost[i]
            if remaining < 0: #negative 
                candidate = i + 1 
                prev_remianing += remaining
                remaining = 0 
        if candidate == len(gas) or remaining + prev_remianing < 0:
            return -1 
        return candidate
        