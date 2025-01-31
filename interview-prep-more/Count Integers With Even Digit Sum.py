class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for num in range(2, num+1):

            cur_sum = 0
            cur_num = num
            while cur_num != 0:
                rem = cur_num % 10
                cur_sum += rem

                cur_num = cur_num // 10

            if cur_sum % 2 == 0:
                count += 1
        
        return count

        
