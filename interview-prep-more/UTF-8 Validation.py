class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        storeCount = 0

        for byte in data:
            temp = 128  # 0b10000000
            count = 0

            # Count leading ones in current byte
            while byte & temp != 0:
                count += 1
                temp >>= 1

            if count > 4:
                return False
            elif count > 1:
                if storeCount != 0:
                    return False
                storeCount = count - 1
            elif count == 0:
                if storeCount != 0:
                    return False
            else:
                if storeCount >= 1:
                    storeCount -= 1
                else:
                    return False

        return storeCount == 0
