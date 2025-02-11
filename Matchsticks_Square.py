# Approach:
# 1. The total sum of all matchsticks must be divisible by 4; otherwise, forming a square is impossible.
# 2. Use backtracking to try forming 4 equal sides.
# 3. Sort matchsticks in descending order to improve efficiency by filling larger values first.
# 4. Recursively place each matchstick into one of the four sides if it doesn't exceed the target side length.
# 5. If all matchsticks are used and four equal sides are formed, return True.

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        
        # Step 1: Check if the sum is divisible by 4 (basic feasibility check)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4  # Each side must be this length
        matchsticks.sort(reverse=True)  # Sorting in descending order optimizes backtracking
        
        # Step 2: Initialize four sides with 0 length
        sides = [0] * 4

        def backtrack(index):
            """Recursive function to attempt forming the square."""
            if index == len(matchsticks):  
                # If all matchsticks are placed, check if all four sides are equal
                return all(side == side_length for side in sides)

            for i in range(4):  
                # Try placing the current matchstick in one of the four sides
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]  # Place matchstick
                    if backtrack(index + 1):  
                        return True  # If successful, return True
                    sides[i] -= matchsticks[index]  # Backtrack (remove matchstick)
                
                if sides[i] == 0:  
                    break  # Optimization: Avoid redundant attempts

            return False  # If no valid placement found, return False

        return backtrack(0)  # Start backtracking from the first matchstick

# Time Complexity: O(4^N), where N is the number of matchsticks.
# - The worst case involves attempting to place each matchstick in one of four sides.

# Space Complexity: O(N), due to recursive calls (max depth = N).