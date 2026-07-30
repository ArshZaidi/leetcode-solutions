# Problem: Asteroid Collision
# Problem ID: 735
# Difficulty: Medium
# Language: Python3
# Runtime: 7 ms
# Memory: 20.3 MB
# Synced From: LeetCode
# Date: 2026-07-30

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and asteroid < 0:

                if stack[-1] < -asteroid:
                    stack.pop()

                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False

                else:
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack