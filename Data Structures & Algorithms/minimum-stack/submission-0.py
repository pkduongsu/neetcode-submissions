class MinStack:

    def __init__(self):
        self.content = []

    def push(self, val: int) -> None:
        self.content.append(val)

    def pop(self) -> None:
        self.content.pop()
        print(self.content)

    def top(self) -> int:
        return self.content[len(self.content) - 1]

    def getMin(self) -> int:
        return min(self.content)
        
