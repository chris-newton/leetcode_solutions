class Solution(object):
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False
    
    # k is the current index of word
    def dfs(self, board, word, i , j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != word[k]:
            return False
        c = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, word, i+1, j, k+1) or \
               self.dfs(board, word, i-1, j, k+1) or \
               self.dfs(board, word, i, j+1, k+1) or \
               self.dfs(board, word, i, j-1, k+1)
        board[i][j] = c
        return res
       