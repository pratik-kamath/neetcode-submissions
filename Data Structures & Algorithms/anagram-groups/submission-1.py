class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            counter_letters = {}
            for letter in word:
                if letter in counter_letters:
                    counter_letters[letter] += 1
                else:
                    counter_letters[letter] = 1

            # Dicts can't be keys, so convert to a sorted tuple of (letter, count) pairs
            key = tuple(sorted(counter_letters.items()))

            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        return list(anagrams.values())