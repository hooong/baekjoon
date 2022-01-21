from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if (sum(gas) - sum(cost)) < 0:
            return -1

        tank = 0
        start_idx = 0
        for i in range(n):
            tank += gas[i] - cost[i]

            if tank < 0:
                start_idx = i + 1
                tank = 0
        return start_idx


def test():
    solution = Solution()

    assert solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3
    assert solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
    assert solution.canCompleteCircuit([1, 2, 0, 1, 0], [0, 0, 3, 0, 1]) == 0
    assert solution.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4
