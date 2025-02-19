class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answer = []
        for i in operations:
            if i == "C":
                answer.pop()
            elif i == "D":
                answer.append(2 * answer[-1])
            elif i == "+":
                answer.append(answer[-1] + answer[-2])
            else:
                answer.append(int(i))
        return sum(answer)
