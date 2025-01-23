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
