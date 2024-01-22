import random
from datetime import datetime

from instance import Instance


class Solution:
    def __init__(self, instance: Instance, path: list):
        self.instance = instance
        self.path = path

    def tsp_cost(self):
        cost = 0
        for i in range(0, self.instance.n):
            cost = cost + self.instance.dist[self.path[i - 1]][self.path[i]]
        return cost

    def two_swap(self):
        copy = self.path.copy()
        i, j = random.sample(range(0, self.instance.n), 2)
        copy[i], copy[j] = copy[j], copy[i]
        return Solution(self.instance, copy)

    def three_cycle(self):
        i, j, k = random.sample(range(0, self.instance.n), 3)
        copy = self.path.copy()
        copy[i], copy[j], copy[k] = copy[j], copy[k], copy[i]
        return Solution(self.instance, copy)

    def twotwo_swap(self):
        copy = self.path.copy()
        i, j, k, l = random.sample(range(0, self.instance.n), 4)
        copy[i], copy[j] = copy[j], copy[i]
        copy[k], copy[l] = copy[l], copy[k]
        return Solution(self.instance, copy)

    def __str__(self):
        return "Solution with cost: {}".format(self.tsp_cost()) + "\n" + "Path: {}".format(self.path)

    def save(self):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        with open(f"../solution/solution_{timestamp}.txt", 'w') as f:
            f.write(str(self.tsp_cost()) + "\n")
            for i in self.path:
                f.write(str(i) + "\n")
