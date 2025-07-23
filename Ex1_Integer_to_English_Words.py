# ----------------------------------------------------
# Intuition:
#
# The number is broken into chunks of 3 digits (hundreds), from right to left.
# Each chunk is converted separately and suffixed with its scale (Thousand, Million, etc).
#
# 1. Recursive Approach:
#    - Convert 3-digit chunks recursively using predefined word lists.
#    - Base cases handle <20, <100, <1000 separately.
#    - Append correct scale (Thousand, Million, Billion) as we go.
#    - Time: O(1) (since max num = 2^31 - 1), Space: O(1)
#
# 2. Iterative Approach:
#    - Similar chunk splitting logic.
#    - Instead of recursion, use loops to build the English words iteratively.
#    - Slightly more verbose but stack-friendly.
#    - Time: O(1), Space: O(1)
# ----------------------------------------------------

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Define mappings
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                        "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            # Convert number less than 1000 to words
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return less_than_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0  # to track thousands index

        while num > 0:
            # Process last 3 digits
            if num % 1000 != 0:
                # Convert chunk + scale word + previously accumulated result
                res = helper(num % 1000) + thousands[i] + " " + res
            num //= 1000
            i += 1
        
        # Clean and strip extra spaces
        return ' '.join(res.split())


    # ----------------------------------------------------
    # 2. Iterative approach (alternative)
    # ----------------------------------------------------
    def numberToWordsIterative(self, num: int) -> str:
        if num == 0:
            return "Zero"

        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                        "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]

        def convert_chunk(n: int) -> str:
            res = ""
            if n >= 100:
                res += less_than_20[n // 100] + " Hundred "
                n %= 100
            if n >= 20:
                res += tens[n // 10] + " "
                n %= 10
            if n > 0:
                res += less_than_20[n] + " "
            return res

        res = ""
        i = 0

        while num > 0:
            if num % 1000 != 0:
                chunk = convert_chunk(num % 1000)
                res = chunk + thousands[i] + " " + res
            num //= 1000
            i += 1

        return ' '.join(res.split())

# ----------------------------------------------------
# Example Usage
# ----------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberToWords(123))           # "One Hundred Twenty Three"
    print(sol.numberToWords(12345))         # "Twelve Thousand Three Hundred Forty Five"
    print(sol.numberToWords(1234567))       # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    print(sol.numberToWords(1000010))       # "One Million Ten"
    print(sol.numberToWords(0))             # "Zero"