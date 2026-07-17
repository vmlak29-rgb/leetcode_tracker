# Last updated: 17/07/2026, 15:01:50
class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total_gas += diff
            current_gas += diff

            # If current tank becomes negative,
            # this starting point cannot work
            if current_gas < 0:
                start = i + 1
                current_gas = 0

        # Total gas available is less than total cost
        if total_gas < 0:
            return -1

        return start