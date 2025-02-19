class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        sn = len(image[0])

        for i in range(n):
            r = sn - 1
            l = 0

            while l <= r:
                # Flip and invert simultaneously using XOR
                image[i][l], image[i][r] = image[i][r] ^ 1, image[i][l] ^ 1
                r -= 1
                l += 1

        return image
