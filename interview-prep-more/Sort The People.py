class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = []
        for i in range(len(heights)):
            max_height  = max(heights)
            get_index = heights.index(max_height)
            result.append(names[get_index])
            del names[get_index]
            del heights[get_index]
        return result
