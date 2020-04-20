# Binary search

When searching in a sorted list the best one can do for speed is O(log(n)), using binary search.

This is a recursive algorithm that works by setting left and right to the index of the edges of the array and calculating the middle with:

```
mid = left + (right - left) / 2
```

If the number at the middle index is greater than the number being searched for, then look at the left side of the array by setting `right = mid` in the next invocation. Otherwise set `left = mid`.
