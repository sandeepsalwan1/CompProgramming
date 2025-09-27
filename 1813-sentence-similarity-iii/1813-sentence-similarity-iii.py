class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        w1 = sentence1.split()
        w2 = sentence2.split()

        if len(w1)> len(w2):
            w1,w2=w2,w1
        l1 = 0
        while l1 < len(w1) and w1[l1]==w2[l1]:
            l1+=1

        l2,r2 =len(w1)-1, len(w2)-1
        while l2 >= 0 and r2>= 0 and w1[l2]==w2[r2]:
            l2-=1
            r2-=1

        return l1 > l2











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
