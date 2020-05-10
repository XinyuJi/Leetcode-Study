n = 9
a = []

b = 1
a.append(1)
while(n - sum(a) > a[-1]):
    a.append(a[-1]+1)
a[-1] = a[-1] + (n-sum(a))
print(a)
        
