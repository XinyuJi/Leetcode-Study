class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_cur = max_glob = min_cur = min_glob = A[0]
        for a in A[1:]:
            max_cur = max(a, a + max_cur)
            max_glob = max(max_glob, max_cur)
            min_cur = min(a, a+min_cur)
            min_glob = min(min_glob, min_cur)
        if sum(A) == min_glob:
            return max_glob
        return max(max_glob, sum(A)-min_glob)
