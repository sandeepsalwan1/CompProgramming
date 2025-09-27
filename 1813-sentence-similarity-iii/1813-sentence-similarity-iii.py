class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        w1 = sentence1.split()
        w2 = sentence2.split()

        # If same length but not identical, can't fix by adding words to ends
        if len(w1) == len(w2):
            return False

        # Make sure w_short is the shorter list of words
        w_short, w_long = (w1, w2) if len(w1) < len(w2) else (w2, w1)

        # Match prefix
        i = 0
        while i < len(w_short) and w_short[i] == w_long[i]:
            i += 1

        # Match suffix
        j = 0
        while j < (len(w_short) - i) and w_short[-1 - j] == w_long[-1 - j]:
            j += 1

        # All words in the shorter must be covered by prefix+suffix matches
        return i + j == len(w_short)
