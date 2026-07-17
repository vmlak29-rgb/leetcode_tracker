# Last updated: 17/07/2026, 15:03:57
class Solution:
    def divide(self, dividend, divisor):

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Find sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Binary division
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp = temp << 1
                multiple = multiple << 1

            dividend -= temp
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        # 32-bit integer range check
        if quotient > INT_MAX:
            return INT_MAX

        if quotient < INT_MIN:
            return INT_MIN

        return quotient