class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}
        return sum([d[val] for val in operations])
