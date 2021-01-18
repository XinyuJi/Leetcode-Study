nums1 = [1,5]
nums2 = [3]
if not nums1:
    num = nums2
elif not nums2:
    num = nums1
else:
    num = sorted(nums1 + nums2)
    print(num)
if len(num)%2 == 0:
    print((float(num[len(num)/2-1]) + float(num[len(num)/2]))/2)
else:
    print(float(num[(len(num)+1)/2-1]))