# CSCI 3412 Homework 4
## Question 1:
### a.
We will be using the min-heap data structure to merge it k sorted list. Each value will be stored as a tuple (value, sublist[ID], next value in sublist). 

**Algorithm**
1. We pull the first (smallest) value from each sublist and put in the heap. Then call the min_heapify() operation to maintain the min-heap property This operation is log(k) because there are k values in the min-heap.
2. Pop the root (min) value from the min-heap and it to the merged list. Then add the next element from same list of previously popped elemented to the min-heap.
3. Repeat step 2 until the k lists are merged.

**Time Complexity**
Each time we pop the minimum element from the heap, we call the min_heapify() function which restores the min-heap property. This operation takes log(k) time due to the height of the binary tree being log(k). There are n elements, thus the total time complexity to merge the k sorted list is nlog(k).
