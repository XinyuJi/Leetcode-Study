'''
Runtime: 112 ms, faster than 15.87% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.5 MB, less than 97.54% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)


# '''
# create a new list
# '''

# list1 = [1,1,2]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print (list2)