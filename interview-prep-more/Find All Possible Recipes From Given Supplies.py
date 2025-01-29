class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indeg = defaultdict(int)
        graph = defaultdict(list)
        for r, ing in zip(recipes, ingredients): 
            indeg[r] = len(ing)
            for i in ing: graph[i].append(r)
        
        ans = []
        queue = deque(supplies)
        recipes = set(recipes)
        while queue: 
            x = queue.popleft()
            if x in recipes: ans.append(x)
            for xx in graph[x]: 
                indeg[xx] -= 1
                if indeg[xx] == 0: queue.append(xx)
        return ans 
