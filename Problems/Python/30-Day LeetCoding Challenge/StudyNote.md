# 30-Day LeetCoding Challenge
## Day 1 - [136] Single Number
- Approach 1: List operation

- Approach 2: Hash Table

- Approach 3: Math
Concept:
2 * (a + b + c) - (a + a + b + b + c) =c

- Approach 4: Bit Manipulation
Concept:
If we take XOR of zero and some bit, it will return that bit
a ^ 0 = a
If we take XOR of two same bits, it will return 0
a ^ a = 0
a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
So we can XOR all bits together to find the unique number.

Related Problem:
- [137] Single Number II
- [260] Single Number III
https://blog.csdn.net/wlwh90/article/details/89712795


## Day 2 - [202] Happy Number

Related Problem:
- [263] Ugly Number