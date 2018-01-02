__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Standard chess rules apply - queens can move along a row or a column or a diagonal.
Given a placement of queens on a nxn board, the placement is considered safe no two queens can kill each other.

Input (board) is a list of queen column positions (ie) if board[i] = j. It means queen in ith column is placed
in jth row. For nxn chessboard, you have rows 0..n-1 and cols 0..n-1.

E.x. if board = [0, 1, 2] it is equivalent to following chessboard:

_ _ Q
_ Q _
Q _ _

Additional notes:

1. ValueError on none or empty list or if list input contains non integers
2. TypeError if board is not a list
3. Return False if board is not a valid placement (for e.g contains column as 5 for a 4x4 chessboard) or if
   2 queens can kill each other
4. Returns True if no 2 queens can kill each other.
'''
def safe_chessboard(board):
    pass

#write your own tests
def test_safe_chessboard():
    pass

