class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def f(c):
            return ord(c) - 97

        st_s1 = [0] * 26
        st_s2 = [0] * 26
        for c in s1:
            st_s1[f(c)] += 1
            
        k = len(s1) -1 
        for c in s2[:k]:
            st_s2[f(c)] += 1
            
        for i, c in enumerate(s2[k:]):
            st_s2[f(c)] += 1
            if st_s1 == st_s2:
                return True
            st_s2[f(s2[i])] -= 1
        return False
