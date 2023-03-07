# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 01:09:19 2023

@author: anete
"""

boardNotFinished = [
    [' ', ' ', ' ', 'B', 'R'],
    [' ', ' ', ' ', 'R', ' '],
    ['G', 'G', 'G', ' ', 'G'],
    [' ', 'B', 'B', ' ', 'G'],
    [' ', ' ', 'R', ' ', ' ']
]

boardFinished = [
    [' ', ' ', 'R', 'B', 'R'],
    ['R', 'B', 'B', 'R', ' '],
    ['G', 'G', 'G', ' ', 'G'],
    ['G', 'B', 'B', 'B', 'G'],
    ['R', ' ', 'R', ' ', 'R']
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