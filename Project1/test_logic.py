# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 01:09:19 2023

@author: anete
"""

boardLose = [
    [' ', ' ', ' ', 'B', 'R'],
    [' ', ' ', ' ', 'R', ' '],
    ['G', 'G', 'G', ' ', 'G'],
    [' ', 'B', 'B', ' ', 'G'],
    [' ', ' ', 'R', ' ', ' ']
]

boardWin = [
    [' ', ' ', 'R', 'B', 'R'],
    ['R', 'B', 'B', 'R', ' '],
    ['G', 'G', 'G', ' ', 'G'],
    ['G', 'B', 'B', 'B', 'G'],
    ['R', ' ', 'R', ' ', 'R']
]

boardTest = [
    [' ', ' ', 'R', 'B', 'R'],
    ['R', 'B', 'B', 'R', ' '],
    ['G', 'G', 'G', ' ', 'G'],
    ['G', 'B', 'B', 'B', 'G'],
    [' ', ' ', 'R', ' ', 'R']
]

board3x3 = [
    [' ', ' ', 'R'],
    [' ', 'B', 'B'],
    [' ', 'G', ' ']
]

board4x4 = [
    [' ', 'R', 'R', 'B'],
    ['R', 'B', 'B', 'R'],
    ['G', 'G', 'G', ' '],
    [' ', 'B', 'B', 'B'],
    ['R', ' ', 'R', ' ']
]


boardTest6x6Initial = [
    ['G', ' ', ' ', ' ', ' ', ' ', 'G'],
    [' ', 'R', 'B', 'B', ' ', ' ', 'G'],
    [' ', 'B', ' ', ' ', 'G', 'G', ' '],
    ['R', ' ', 'R', 'R', ' ', ' ', ' '],
    [' ', 'G', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'G', 'G', ' ', ' ', ' ']
]

boardTest6x6Test = [
    ['G', ' ', 'G', ' ', 'G', 'G'],
    ['G', 'R', 'B', 'B', 'R', 'G'],
    [' ', 'B', ' ', ' ', 'G', 'B'],
    ['R', 'R', 'R', 'R', 'R', ' '],
    ['G', 'G', 'B', 'B', 'G', 'G'],
    ['G', ' ', 'G', 'G', ' ', 'G']
]


boardComplete = [
    ['R', 'B', 'R', 'B', 'R'],
    ['R', 'B', 'B', 'R', 'G'],
    ['G', 'G', 'G', 'R', 'G'],
    ['G', 'B', 'B', 'B', 'G'],
    ['R', 'G', 'R', 'R', 'R']
]

def verifyListPalindrome(boardLine):
        return boardLine == boardLine[::-1]

    
"""
Makes a transpose board to get the columns as lines

Teste
>>> board1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> transposeBoard(board1)
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

"""    
def transposeBoard(board):
    return [list(row) for row in zip(*board)]
    

def eliminateBlankSpaces(board):
    return  [[elem for elem in row if elem != ' '] for row in board]


def boardFull(board):
    for row in board:
        for piece in row:
            if piece == ' ':
                return False
    return True
    
"""
verify if game ended by checking if all rows and columns are palindromes

Test
- board = [[1, 2, 3, 2, 1], [4, 5, 6, 5, 4], [7, 8, 9, 8, 7], [4, 5, 6, 5, 4], [1, 2, 3, 2, 1]]
- verifyGameEnd(board)
True
"""
def verifyGameEnd(board):

        
    # see if all rows are palindromes
    cleanRows = eliminateBlankSpaces(board)
    rowsPalindrome = True
    for row in cleanRows:
        if not verifyListPalindrome(row):
            rowsPalindrome = False
            break
    
    
    # see if all columns are palindromes
    cleanColumns = eliminateBlankSpaces(transposeBoard(board))
    columnsPalindrome = True
    for col in cleanColumns:
        if not verifyListPalindrome(col):
            columnsPalindrome = False
            break
    
    return rowsPalindrome and columnsPalindrome
    


def getUserInput(maxSize):
    color = input("Choose a color(R-red, G-green, B-blue): ").upper()
    while color not in {'R', 'G', 'B'}:
        print("Invalid color. Please choose between R, G or B")
        color = input("Choose a color(R, G, B): ").upper()
    
    row = input(f"Choose a row(number between 0 and {maxSize-1}): ")  
    while not row.isdigit() or int(row) not in range(maxSize):
        print(f"Invalid row. Please choose a number between 0 and {maxSize-1}): ")
        row = input(f"Choose a row(number between 0 and {maxSize-1}): ") 
        
    column = input(f"Choose a column(number between 0 and {maxSize-1}): ")
    while not column.isdigit() or int(column) not in range(maxSize):
        print(f"Invalid column. Please choose a number between 0 and {maxSize-1}): ")
        column = input(f"Choose a column(number between 0 and {maxSize-1}): ") 
    
    return color, int(row), int(column)
    

# def mergeBlankAndPalindrome(board):

def verifyInCanPutPiece(board, row, col):    
    if board[row][col] != ' ':
        return False
    elif len(board) < row or len(board) < col:
        return False
    elif row < 0 or col < 0:
        return False
    return True
    

def putPieceInBoard(board, color, row, column):
    start = (2, 2)
    end = (4, 4)
    path = bfs(board, start, end)
    if path:
        print("Path Found:", path)
    else:
        print("Path Not Found")
    maxSize = len(board[0])
    #color, row, column = getUserInput(maxSize)
    if verifyInCanPutPiece(board, row, column):
        board[row][column] = color
        return board
    else:
        print("Invalid input, please choose an empty space")
    
 
def gameLoop(board):
    newBoard = putPieceInBoard(board)
    if verifyGameEnd(newBoard):
        print("Jogo terminado")
        return True
    gameLoop(newBoard) 

def bfs(board, start, end):
    queue = [(start, [start])]
    visited = set([start])
    while queue:
        (current_x, current_y), path = queue.pop(0)
        if (current_x, current_y) == end:
            return path
        # Check for palindrome line
        if board[current_x] == board[current_x][::-1] and (current_x, 0) not in visited:
            queue.append(((current_x, 0), path + [(current_x, 0)]))
            visited.add((current_x, 0))
        # Check for palindrome column
        if all(board[i][current_y] == board[~i][current_y] for i in range(len(board))) and (0, current_y) not in visited:
            queue.append(((0, current_y), path + [(0, current_y)]))
            visited.add((0, current_y))
        # Add adjacent nodes
        for x, y in get_adjacent_nodes(board, current_x, current_y):
            if (x, y) not in visited:
                queue.append(((x, y), path + [(x, y)]))
                visited.add((x, y))
    return None

def get_adjacent_nodes(board, current_x, current_y):
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    adj_nodes = []
    for dx, dy in directions:
        x, y = current_x + dx, current_y + dy
        if x >= 0 and x < rows and y >= 0 and y < cols and board[x][y] != " ":
            adj_nodes.append((x, y))
    return adj_nodes