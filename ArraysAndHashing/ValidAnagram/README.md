# [217. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and return `false` otherwise.

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```
#### Constraints:

* `1 <= s.length, t.length <= 5 * 104`

+ ` `s` and `t` consist of lowercase English letters.`

# Solution

#### Pseudo code
```c
Algorithm:
Inputs: s, t: String of char;
Returns: Bool
Variables: 

Begin
  selectionSort(s)
  selctionSort(t)
  if s == t then
    return true

  return false
End
```
#### Commentatory

#### Complexity Analysis
+ Time Complexity: O(N^2)
+ Space Complexity: O(1)
