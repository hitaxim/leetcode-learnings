from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def neighbors(node):
            for i in range(len(node)):
                for g in ["A", "C", "G", "T"]:
                    if node[i] != g:
                        yield f"{node[:i]}{g}{node[i + 1:]}"

        bank = set(bank)
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        seen = {startGene}

        while queue:
            node, step = queue.popleft()
            if node == endGene:
                return step

            for n in generate_neighbors(node):
                if n not in seen and n in bank:
                    seen.add(n)
                    queue.append((n, step + 1))

        return -1
