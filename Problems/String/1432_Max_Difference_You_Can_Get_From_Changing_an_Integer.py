class Solution:
    def maxDiff(self, num: int) -> int:
        maxn = minn = str(num)
        for i in maxn:
            if i != '9':
                maxn = maxn.replace(i, '9')
                break
                
        if minn[0] != '1':
            minn = minn.replace(minn[0], '1')
        else:
            for i in minn[1:]:
                if i not in "01":
                    minn = minn.replace(i, '0')
                    break
        
        return int(maxn) - int(minn)
