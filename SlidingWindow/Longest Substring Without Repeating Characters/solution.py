class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Declare right and left pointers for sliding window
        right, left = 0, 0
        #holds max value for this instance of the method
        global_max = 0
        hashmap = dict()
        
        #iterate through the string
        while right < len(s):
            #current char at right pointer
            curr = s[right]
            #if char not in dictionary add it as key woith value of 0
            if curr not in hashmap:
                hashmap[curr] = 0
            #increase the value of char by 1
            hashmap[curr] += 1
            #If there are any chars with value greater than 1 
            #i.e. there are duplicates shrink the winddow and decremnt the value at the left pointer
            if any(v > 1 for v in iter(hashmap.values())):
                hashmap[s[left]] -= 1
                left += 1
            #check if global max is greater than the window size
            global_max = max(global_max, right - left + 1)
            right += 1
            
        return global_max