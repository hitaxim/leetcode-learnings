class Solution:
    def check(self, num):
        st = str(num)
        if '0' in st: return False
        for i in range(len(st)):
            if num % int(st[i]): return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret_arr = []
        for i in range(left, right+1):
            if self.check(i):
                ret_arr.append(i)
        return ret_arr
