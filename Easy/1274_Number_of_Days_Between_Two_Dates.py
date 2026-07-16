# Problem: Number of Days Between Two Dates
# Problem ID: 1274
# Difficulty: Easy
# Language: Python
# Runtime: 3 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def daysBetweenDates(self, date1, date2):
        def isLeap(year):
            return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

        def days(date):
            year, month, day = map(int, date.split("-"))

            monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            total = 0

            for y in range(1971, year):
                total += 366 if isLeap(y) else 365

            for m in range(month - 1):
                total += monthDays[m]
                if m == 1 and isLeap(year):
                    total += 1

            total += day

            return total

        return abs(days(date1) - days(date2))