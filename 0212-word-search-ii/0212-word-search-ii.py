class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        # 1) Build trie
        trie = {}
        END = '#'
        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch, {})
            node[END] = w

        res = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # 2) Single DFS over the whole board
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return
            nxt = node[ch]
            # found a word
            if END in nxt:
                res.append(nxt[END])
                nxt.pop(END)      # avoid duplicates

            board[r][c] = None  # mark visited
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] is not None:
                    dfs(nr, nc, nxt)
            board[r][c] = ch   # un-mark

            # prune leaf
            if not nxt:
                node.pop(ch)

        # 3) Launch DFS from each cell
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, trie)

        return res