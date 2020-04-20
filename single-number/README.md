# Single Number
Part of Leetcodes 30 days of code in April 2020, problem is:

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

```
Input: [2,2,1]
Output: 1
```

Example 2:

```
Input: [4,1,2,1,2]
Output: 4
```

## Ideas
Two data structures that come to mind are 
* dictionaries
* sets


## Brute force

1. Sort
2. enumerate every other number, check if it's the same as the one to the right of it or if it's the last one


## Ideal solution


