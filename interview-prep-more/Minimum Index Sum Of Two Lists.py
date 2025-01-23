class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_one = {}
        hash_two = {}
        for index in range(len(list1)):
            hash_one[list1[index]] = index
        
        for index in range(len(list2)):
            hash_two[list2[index]] = index
        
        sums = defaultdict(list)
        for key, value in hash_one.items():
            if key in hash_two:
                index_sum = value + hash_two[key]
                sums[index_sum].append(key)
        return sums[min(sums)]

"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    indexsum = i + j
                    count[list1[i]] = indexsum
        min_indexsum = min(count.values())
        ans = []
        for key,val in count.items():
            if val == min_indexsum:
                ans.append(key)
        return ans

    """
