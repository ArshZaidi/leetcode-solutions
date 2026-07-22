# Problem: Validate IP Address
# Problem ID: 468
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-07-22

class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        # Check IPv4
        if queryIP.count('.') == 3:
            parts = queryIP.split('.')

            for part in parts:
                if len(part) == 0:
                    return "Neither"

                if not part.isdigit():
                    return "Neither"

                if len(part) > 1 and part[0] == '0':
                    return "Neither"

                if int(part) < 0 or int(part) > 255:
                    return "Neither"

            return "IPv4"

        # Check IPv6
        if queryIP.count(':') == 7:
            parts = queryIP.split(':')

            hex_digits = "0123456789abcdefABCDEF"

            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return "Neither"

                for ch in part:
                    if ch not in hex_digits:
                        return "Neither"

            return "IPv6"

        return "Neither"