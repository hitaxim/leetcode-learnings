class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        blocked = defaultdict(set)

        
        for row, col in reservedSeats:
            if col in [2, 3, 4, 5]:
                blocked[row].add('left')
            if col in [4, 5, 6, 7]:
                blocked[row].add('middle')
            if col in [6, 7, 8, 9]:
                blocked[row].add('right')
        
        total = 2 * (n - len(blocked))
        numAvailable = {0: 2, 1: 1, 2: 1, 3: 0}

        for numBlocked in blocked.values():
            total += numAvailable[len(numBlocked)]

        return total
        
"""
class Solution:
	def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
		seats = collections.defaultdict(set)

		for i,j in reservedSeats:
			if j in [2,3,4,5]:
				seats[i].add(0)
			if j in [4,5,6,7]:
				seats[i].add(1)
			if j in [6,7,8,9]:
				seats[i].add(2)
		res = 2*n
		for i in seats:
			if len(seats[i]) == 3:
				res -= 2
			else:
				res -= 1

		return res
"""     
