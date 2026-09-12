class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for x in operations:
            if x != "+" and x != "D" and x != "C":
                record.append(int(x))
            elif x == "+":
                record.append(record[-1] + record[-2])
            elif x == "D":
                record.append(record[-1] * 2)
            elif x == "C":
                record.pop()
        return sum(record)
            