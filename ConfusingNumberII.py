class Solution:
    def confusingNumberII(self, n: int) -> int:
        # Approach:
        # 1. Use a backtracking approach to generate numbers from valid digits (0,1,6,8,9).
        # 2. For each generated number, check if it forms a different valid number when rotated 180 degrees.
        # 3. Count numbers that meet the "confusing" criteria.
        # 4. Stop recursion if the generated number exceeds 'n'.

        # Valid digit mappings when rotated 180 degrees
        valid_digits = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.count = 0  # Counter for confusing numbers

        def is_confusing(num):
            """Check if rotating 'num' 180 degrees results in a different number."""
            original = num
            rotated = 0
            while num > 0:
                digit = num % 10
                rotated = rotated * 10 + valid_digits[digit]
                num //= 10
            return rotated != original  # Confusing if rotated number differs

        def backtrack(curr_num):
            """Generate numbers using valid digits and count confusing ones."""
            if curr_num > n:
                return  # Stop if number exceeds 'n'

            if curr_num > 0 and is_confusing(curr_num):
                self.count += 1  # Increment count if confusing

            for digit in valid_digits:
                new_num = curr_num * 10 + digit
                if new_num > 0:  # Avoid leading zeros
                    backtrack(new_num)  # Recursive call for next digit

        backtrack(0)  # Start recursion from 0
        return self.count  # Return total count of confusing numbers

# Time Complexity: O(logN)
# - Each number is generated recursively and checked if confusing, but the branching factor is low.

# Space Complexity: O(logN)
# - Recursive depth is limited by the length of 'n' in digits.