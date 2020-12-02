def atmostk(self, A, K):
        i = res = 0
        counter = collections.defaultdict(int)
        for j in range(len(A)):
            counter[A[j]] += 1
            while len(counter) > K:
                counter[A[i]] -= 1
                if counter[A[i]] == 0:
                    del counter[A[i]]
                i += 1
            res = max(res, j-i+1)
        return res
