class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            canon = "".join(sorted(word))
            if canon not in group:
                group[canon] = []
            group[canon].append(word)
        return list(group.values())