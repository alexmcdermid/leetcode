
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


class Solution:
    def isIsomorphic(s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for x,y in zip(s,t):
            if (x not in map1) and (y not in map2):
                map1[x] = y
                map2[y] = x
            elif map1.get(x) != y or map2.get(y) != x:
                return False
        
        return True


# Example 1:

# Input: s = "egg", t = "add"
# Output: true
print(Solution.isIsomorphic('egg','add'))


# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
print(Solution.isIsomorphic('foo','bar'))

# Example 3:

# Input: s = "paper", t = "title"
# Output: true
print(Solution.isIsomorphic('paper','title'))
