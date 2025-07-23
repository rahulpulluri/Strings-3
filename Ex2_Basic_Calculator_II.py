# ----------------------------------------------------
# Intuition:
#
# 1. Optimized Approach (No Stack):
#    - Use variables to track the total result, the last number, and current number.
#    - When encountering + or -, add the last number to total, and update last_num.
#    - For * or /, update last_num by multiplying or dividing.
#    - This way, * and / have precedence since they modify last_num before adding to total.
#    - Time: O(n), Space: O(1)
#
# 2. Stack-Based Approach:
#    - Use a stack to store numbers and their signs.
#    - On '+' or '-', push number (positive or negative).
#    - On '*' or '/', pop last number, apply operation, and push result back.
#    - Sum stack at the end.
#    - Easier to implement but uses O(n) space.
#    - Time: O(n), Space: O(n)
# ----------------------------------------------------

from typing import List

class Solution:

    # ----------------------------------------------------
    # 1. Optimized Approach (No Stack)
    # Time: O(n), Space: O(1)
    # ----------------------------------------------------
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")  # remove spaces
        n = len(s)
        total = 0       # running total sum of evaluated terms
        last_num = 0    # last number to handle * and /
        num = 0         # current parsed number
        prev_op = '+'   # track previous operator (default to '+')

        for i in range(n):
            char = s[i]

            if char.isdigit():
                num = num * 10 + int(char)  # parse multi-digit number

            # if char is operator or end of string, evaluate based on prev_op
            if not char.isdigit() or i == n - 1:
                if prev_op == '+':
                    total += last_num    # add last number to total
                    last_num = num       # update last_num to current number
                elif prev_op == '-':
                    total += last_num
                    last_num = -num
                elif prev_op == '*':
                    last_num = last_num * num
                elif prev_op == '/':
                    last_num = int(last_num / num)  # truncate toward zero
                
                prev_op = char   # update previous operator
                num = 0          # reset current number
        
        total += last_num  # add last pending number
        return total

    # ----------------------------------------------------
    # 2. Stack-Based Approach
    # Time: O(n), Space: O(n)
    # ----------------------------------------------------
    def calculate_stack(self, s: str) -> int:
        s = s.replace(" ", "")  # remove spaces
        stack = []
        num = 0
        prev_op = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            # when hitting operator or end, evaluate previous operator
            if not char.isdigit() or i == len(s) - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))  # truncate toward zero
                
                prev_op = char
                num = 0

        return sum(stack)

# ----------------------------------------------------
# Example Usage
# ----------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("3+2*2"))      # 7
    print(sol.calculate(" 3/2 "))      # 1
    print(sol.calculate(" 3+5 / 2 "))  # 5

