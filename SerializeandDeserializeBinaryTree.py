from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        stack = deque()
        node = root
        while node or stack:
            if node:
                res.append(str(node.val))
                stack.append(node)
                node = node.left
            else:
                res.append("#")
                node = stack.pop().right
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:return None
        strList = data.split(",")
        pre = TreeNode(int(strList[0]))
        root = pre
        stack = deque()
        for i in range(1, len(strList)):
            n = strList[i]
            if pre:
                if n == "#":
                    stack.append(pre)
                    pre = None
                else:
                    print(n)
                    pre.left = TreeNode(int(n))
                    stack.append(pre)
                    pre = pre.left
            else:
                pre = stack.pop()
                if n != "#":
                    pre.right = TreeNode(int(n))
                    pre = pre.right
        return root
if __name__ == "__main__":
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.right.left = TreeNode(4)
    node.right.left = TreeNode(5)
    s = Codec()
    string = s.serialize(node)
    print(string)
    s.deserialize(string)
