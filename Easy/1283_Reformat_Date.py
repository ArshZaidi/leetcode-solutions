# Problem: Reformat Date
# Problem ID: 1283
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def reformatDate(self, date):
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        day, month, year = date.split()
        day = day[:-2].zfill(2)

        return year + "-" + months[month] + "-" + day