dic = {1:3, 2:1, 3:2}
count = 0
for num in dic:
    val = dic[num]
    for i in range(val):
        count += i
        print(num, count)