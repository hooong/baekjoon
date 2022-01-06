from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dest_passengers = {}

        trips.sort(key=lambda x: (x[1]))

        i = 0
        while trips:
            if i in dest_passengers.keys():
                capacity += dest_passengers[i]
                del(dest_passengers[i])

            while trips and i == trips[0][1]:
                cur_passengers, f, t = trips.pop(0)

                if capacity < cur_passengers:
                    return False

                capacity -= cur_passengers
                if t in dest_passengers.keys():
                    dest_passengers[t] += cur_passengers
                else:
                    dest_passengers[t] = cur_passengers

            i += 1

        return True


def test():
    solution = Solution()

    assert solution.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4) is False
    assert solution.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5) is True
