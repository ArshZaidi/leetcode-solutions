# Problem: String Compression
# Problem ID: 443
# Difficulty: Medium
# Language: Python3
# Runtime: 1 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-07-22

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[write] = chars[i - 1]
                write += 1

                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                count = 1

        return write