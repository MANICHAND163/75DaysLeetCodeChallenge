class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map= {}
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        for s in strs:
            key="".join(sorted(s))
            if key not in anagram_map:
                anagram_map[key]= []
            anagram_map[key].append(s)
        return list(anagram_map.values())

