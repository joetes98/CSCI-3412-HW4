import random
import time
import bisect
import numpy as np

# Skip List Node
class SkipListNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

# Skip List Class
class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipListNode(None, self.max_level)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.value != value:
            new_level = self.random_level()
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            new_node = SkipListNode(value, new_level)
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, value):
        current = self.header
        ops = 0
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
                ops += 1  # comparison + forward step
            ops += 1  # comparison failed or succeeded at this level
        current = current.forward[0]
        found = current is not None and current.value == value
        ops += 1  # final comparison
        return found, ops

# Simulate number of comparisons in binary search
def binary_search_ops(sorted_list, value):
    left, right = 0, len(sorted_list) - 1
    ops = 0
    while left <= right:
        mid = (left + right) // 2
        ops += 1
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return ops

# Benchmarking
def benchmark_skiplist_vs_binarysearch(trials=10, size=1_000_000, range_max=1_000_000):
    skip_times = []
    binary_times = []
    skip_ops_all = []
    binary_ops_all = []

    for _ in range(trials):
        data = random.sample(range(range_max), size)
        data.sort()

        # Skip List
        skiplist = SkipList()
        for num in data:
            skiplist.insert(num)

        search_data = random.sample(range(range_max), size)

        # Skip list search
        start_time = time.time()
        skip_ops = 0
        for num in search_data:
            _, ops = skiplist.search(num)
            skip_ops += ops
        skip_times.append(time.time() - start_time)
        skip_ops_all.append(skip_ops)

        # Binary search
        start_time = time.time()
        binary_ops = 0
        for num in search_data:
            binary_ops += binary_search_ops(data, num)
        binary_times.append(time.time() - start_time)
        binary_ops_all.append(binary_ops)

    return skip_times, binary_times, skip_ops_all, binary_ops_all

# Run the benchmark and print the results
skip_times, binary_times, skip_ops_all, binary_ops_all = benchmark_skiplist_vs_binarysearch()
print("Skip List Search Times:", skip_times)
print("Binary Search Times:", binary_times)
print("Average Skip List Search Time:", np.mean(skip_times))
print("Average Binary Search Time:", np.mean(binary_times))
print("Skip List Operations per Trial:", skip_ops_all)
print("Binary Search Operations per Trial:", binary_ops_all)
print("Average Skip List Operations:", np.mean(skip_ops_all))
print("Average Binary Search Operations:", np.mean(binary_ops_all))
