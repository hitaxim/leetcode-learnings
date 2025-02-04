class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        num = abs(numerator)
        denom = abs(denominator)
        remainder = num % denom

        result.append(str(num // denom))

        if remainder == 0:
            return "".join(result)

        result.append(".")
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denom))
            remainder %= denom

        return "".join(result)
