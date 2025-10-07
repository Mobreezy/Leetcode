# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```
#### Constraints:

* `1 <= nums.length <= 105`

+ `-109 <= nums[i] <= 109`

# Solution

#### Pseudo code
```c
Algorithm:
Inputs: nums: Array of Integers; numsSize: Size of Array
Returns: Bool
Variables: 

Begin
  quickSort(nums)
  for i:=0 to numsSize - 1 do
    if nums[i] == nums[i + 1] then
      return true

  return false
End
```
#### Commentatory

#### Complexity Analysis
+ Time Complexity: O(N log(N))
+ Space Complexity: O(1)



### Running the test cases

``` bash
clang -o test test.c
./test
```