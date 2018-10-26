class Solution:
    def __init__(self):
        self.stack = []
    def push(self, node):
        # write code here
        if not self.stack:
            self.stack.append((node, node))
        else:
            self.stack.append((node, min(node, self.stack[-1][-1])))
    def pop(self):
        # write code here
        return self.stack[-1][0]
    def top(self):
        # write code here
        pop = self.stack.pop()
        return pop[0]
    def min(self):
        # write code here
        return self.stack[-1][-1]
