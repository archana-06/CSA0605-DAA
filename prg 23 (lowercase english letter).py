"""You are given a string s. s[i] is either a lowercase English letter or '?'. For a string t having length m
containing only lowercase English letters, we define the function cost(i) for an index i as the number of characters
equal to t[i] that appeared before it, i.e. in the range [0, i - 1]. The value of t is the sum of cost(i) for all indices i.
For example, for the string t = "aab":
cost(0) = 0
cost(1) = 1
cost(2) = 0
Hence, the value of "aab" is 0 + 1 + 0 = 1. Your task is to replace all occurrences of '?' in s with any lowercase
English letter so at the value of s is minimized.
"""
def minimize_string_value(s):
    s = list(s) 
    n = len(s)
    
    for i in range(n):
        if s[i] == '?':
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if (i > 0 and s[i - 1] == ch) or (i < n - 1 and s[i + 1] == ch):
                    continue
                s[i] = ch
                break
    
    return ''.join(s)

s = "a?b?c?"
result = minimize_string_value(s)
print(result)  


