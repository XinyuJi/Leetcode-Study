"""
Runtime: 28 ms, faster than 56.55% of Python3 online submissions for Day of the Week.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Day of the Week.
"""

from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime("%A")
