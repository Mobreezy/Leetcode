# [20. Valid Parenthesis](https://leetcode.com/problems/valid-parentheses/)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example 1:
```
Input: s = "()"
Output: true
```

Example 2:
```
Input: s = "()[]{}"
Output: true
```

Example 3:
```
Input: s = "(]"
Output: false
```

#### Constraints:

* `1 <= s.length <= 10^4`

+ `s` consists of parentheses only '()[]{}'

# Solution

#### Pseudo code
```c
Algorithm: InsertionSort
Inputs: s: String; N:Integer
Variables: i,j,key: Integer
Returns: Bool
Begin 
	for i:=1 to N-1 do
		key:=A[i]
		j:=i;
		while j>0 and key<A[j-1] do
			A[j]:=A[j-1]
			j:=j-1
		A[j]:=key
End
```
#### Commentatory

#### Complexity Analysis
+ Time Complexity: 
+ Space Complexity: 