class Node:
    def __init__(self, val=False):
        self.leaf = False
        self.children = {}


class Solution(object):
    def findWords(self, board, words):
        root = Node()

        for w in words:
            sp = root
            for ch in w:
                if ch in sp.children:
                    sp = sp.children[ch]
                else:
                    sp.children[ch] = Node()
                    sp = sp.children[ch]
            sp.leaf = True

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        maps = [[True for _ in range(len(board[0]))] for _ in range(len(board))]
        ans = set()

        def dfs(cur_loc, tree, _str):
            if tree.leaf:
                ans.add(_str)
                tree.leaf = False  

            for k in range(4):
                tx = cur_loc[0] + dx[k]
                ty = cur_loc[1] + dy[k]
                if 0 <= tx < len(board) and 0 <= ty < len(board[0]):
                    ch = board[tx][ty]
                    if maps[tx][ty] and ch in tree.children:
                        maps[tx][ty] = False
                        child = tree.children[ch]
                        dfs([tx, ty], child, _str + ch)
                        maps[tx][ty] = True

                        if (not child.leaf) and (not child.children):
                            tree.children.pop(ch, None)

        for i in range(len(board)):
            for j in range(len(board[0])):
                ch0 = board[i][j]
                if ch0 in root.children:
                    maps[i][j] = False
                    dfs([i, j], root.children[ch0], ch0)
                    maps[i][j] = True

                    child0 = root.children.get(ch0)
                    if (child0 is not None) and (not child0.leaf) and (not child0.children):
                        root.children.pop(ch0, None)

        return list(ans)
