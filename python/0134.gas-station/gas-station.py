from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        length = len(gas)
        for start_station in range(length):
            for j in range(length):
                cur = (start_station + j) % length
                next_station = (cur + 1) % length
                pass_gas = tank + gas[cur] - cost[cur]
                if pass_gas < 0:
                    # can not go next station
                    # reset tank to a new start station
                    tank = 0
                    break
                else:
                    tank = pass_gas
                    if next_station == start_station:
                        return start_station
        return -1


if __name__ == '__main__':
    solution = Solution()
    res = solution.canCompleteCircuit([1, 2, 3, 4, 5],
                                      [3, 4, 5, 1, 2])
    print(res)
    res1 = solution.canCompleteCircuit([3, 3, 4], [3, 4, 4])
    print(res1)
