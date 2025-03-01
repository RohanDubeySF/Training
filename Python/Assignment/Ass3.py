"""3. Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Constraints:

        - 1 <= strs.length <= 104

        - 0 <= strs[i].length <= 100

        - strs[i] consists of lowercase English letters.

    Example 1:

        - Input: strs = ["eat","tea","tan","ate","nat","bat"]

        - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Example 2:

        - Input: strs = [""]

        - Output: [[""]]

    Example 3:

        - Input: strs = ["a"]

        - Output: [["a"]]
"""

def anagrams(words):
    anag={}
    for word in words:
        a="".join(sorted(word.lower()))
        if a not in anag:
            anag[a]=[]
        anag[a].append(word.lower())
    print(sorted(anag.values()))


anagrams(["eat","Tea","tan","ate","nat","bat"])
        