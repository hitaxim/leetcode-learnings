class Solution:
  def fractionAddition(self, expression: str) -> str:
    ints = list(map(int, re.findall('[+-]?[0-9]+', expression)))
    A = 0
    B = 1

    for a, b in zip(ints[::2], ints[1::2]):
      A = A * b + a * B
      B *= b
      g = math.gcd(A, B)
      A //= g
      B //= g

    return str(A) + '/' + str(B)
        

"""
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1

        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i+1]
            numerator = numerator * den + num * denominator
            denominator *= den 

        common_div = gcd(numerator, denominator)
        return f"{numerator // common_div}/{denominator // common_div}"
"""
