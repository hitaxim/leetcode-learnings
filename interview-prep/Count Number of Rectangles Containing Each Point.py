class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        dict_list = defaultdict(list)

        for l, h in rectangles: 
            dict_list[h].append(l)

        for v in dict_list.values(): 
            v.sort()

        ans = []
        for x, y in points: 
            cnt = 0
            for yy in range(y, 101):
                if yy in dict_list: 
                    cnt += len(dict_list[yy]) - bisect_left(dict_list[yy], x)
            ans.append(cnt)
        return ans
