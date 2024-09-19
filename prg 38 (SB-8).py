class WordFilter:
    def __init__(self, words):
        self.pref_suff_dict = {}
        for index, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                for j in range(n + 1):
                    prefix_suffix = word[:i] + '#' + word[j:]
                    self.pref_suff_dict[prefix_suffix] = index

    def f(self, pref, suff):
        key = suff + '#' + pref
        if key in self.pref_suff_dict:
            return self.pref_suff_dict[key]
        return -1
wordFilter = WordFilter(["apple"])
print(wordFilter.f("a", "e"))  
