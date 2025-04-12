# CSCI 3412 Homework 4
## Question 1:
### a.

**Data Structure**  
We will be using the min-heap data structure to merge it k sorted list. Each value will be stored as a tuple (value, sublist[ID], next value in sublist). 

**Algorithm**
1. Pop the first (smallest) value from each sublist and put in the heap. Then call the min_heapify() operation to maintain the min-heap property This operation is $log_{2}(k)$ because there are k values in the min-heap.
2. Pop the root (min) value from the min-heap and add it to the merged list. Then add the next element from same list of previously popped elemented to the min-heap.
3. Repeat step 2 until the k lists are merged.
  

**Time Complexity**  
Each time we pop the minimum element from the heap, we call the min_heapify() function which restores the min-heap property. This operation takes $log_{2}(k)$ time due to the height of the binary tree being $log_{2}(k)$. There are n elements, thus the total time complexity to merge the k sorted list is $nlog_{2}(k)$.  
  
**Reflections on nk vs nlogk**  

**nlog(k) total time:** 0.3314087390899658 seconds  
**nk total time:** 4.978586435317993 seconds
  
The results show that the nlogk algorithm performs much faster than the nk algorithm. While the nk algorithm is not "slow" as it took under 5 seconds, the time could increase by a large amount if the number of sublists were increased.
  
When I originally implemented the nlogk algorithm, I had written my own functions for minHeapify() and buildMinHeap(). With these functions, I found that my nlogk algorithm was actually performing slower than the nk algorithm. After some testing, I found that this was due to the fact that I was rebuilding the entire heap with buildMinHeap() after every insertion/deletion. Because of this, the operations were much closer to O(k) rather than O(logk). Instead, I used the heapq library that is included with python. Heapq has two methods, $heappush()$ and $heappop()$ which add/remove elements from the min heap while maintaining the heap property. This library helped achieve the desired results.


## Question 2: Skip List Search vs Binary Search: Summary & Observations  
###
**Skip List Search vs Binary Search: Summary & Observations**  
  
Below are the results from the skip list vs binary search experiment. The results are the total time it took to search all 1M elements, and the total number of operations to search for all 1M elements. I asked ChatGPT to count the number of operations, as the number of operations is a better indicator of time efficiency.
  
**Average Skip List Search Time:** 3.4466786861419676  
**Average Binary Search Time:** 0.5164488315582275  
  
**Average Skip List Operations:** 40652490.2  
**Average Binary Search Operations:** 19951425.0  

The binary search algorithm performed exactly as expected. If we divide the total number of operations by the number of searches we get:  $\frac{19,951,425.0}{1,000,000} = 19.951425 \approx log_{2}(1,000,000)$  
  
The skip list search performed slightly worse than the binary search. Dividing the total number of operations by the number of searches we get: $\frac{40,652,490.2}{1,000,000} = 40.6524902 \approx 2log_{2}(1,000,000)$
  
The skip list search took around double the amount of operations as the binary search. While being worse than the binary search, it still follows a logarithmic growth rate, which is much better than the linear time efficiency of a standard linked list. The slightly worse performance of the skip list is most likely due to the randomess of the skip levels, and the overhead that could come from dereferencing the pointers. This is fine because for the skip list, we trade the worse search performance for a better insert performance, as the there a O(1) insert time compared to the static array's O(n) time.
  
  
**Reflection on AI as a tool**  
This exercise proved to me how powerful that ChatGPT (or any AI) is as a tool when coding. I gave ChatGPT the prompt exactly as it's stated on the assignment, and it instantly generated code for me. The code worked exactly as intended the first time it was generated. The only modification that I requested was the inclusion to count the number of operations, but this was not vital to the functionality of the code.  
However it is still best to wary when using AI assistance, as it does not always give the correct answers, especially when provided with more complex problems.
