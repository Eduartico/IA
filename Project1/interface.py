import tkinter as tk
import test_logic as logic
from time import sleep
import algorithms as alg
import levels

# Define the ASCII art title
title = """
   _____                                __            
  / ___/__  ______ ___  ____ ___  ___  / /________  __
  \__ \/ / / / __ `__ \/ __ `__ \/ _ \/ __/ ___/ / / /
 ___/ / /_/ / / / / / / / / / / /  __/ /_/ /  / /_/ / 
/____/\__, /_/ /_/ /_/_/ /_/ /_/\___/\__/_/   \__, /  
     /____/                                  /____/   
"""

# Define the list of available algorithms
algorithms = ["0 - Human Player",
              "1 - BFS",
              "2 - DFS",
              "3 - IDS",
              "4 - Greedy",
              "5 - A*"]


# Create the main window
window = tk.Tk()
window.title("Symmetry")

# Create a label for the title
title_label = tk.Label(window, text=title, font=("Courier", 14))
title_label.pack(side="top", fill="x")

# Create a label and entry for the level
level_label = tk.Label(window, text="Enter level:")
level_label.pack()
level_entry = tk.Entry(window)
level_entry.pack()

# Create a label and option menu for the algorithms
algorithm_label = tk.Label(window, text="Select algorithm:")
algorithm_label.pack()
algorithm_var = tk.StringVar()
algorithm_var.set(algorithms[0])
algorithm_option_menu = tk.OptionMenu(window, algorithm_var, *algorithms)
algorithm_option_menu.pack()

# Create a button for starting the game
start_button = tk.Button(window, text="Start Game")
start_button.pack()

# Create a canvas for drawing game elements
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()
global board
board = logic.boardTest


# Create a function to start the game when the button is clicked
def start_game():
    global board
    try:
        level = int(level_entry.get())
    except ValueError:
        level = 1  # default level if no input,
    if(level > len(levels.levels) or level <=0):
        level = 1
    initial_board = levels.levels[level-1]
    board = initial_board
    option = algorithm_var.get()
    if option == "0 - Human Player":
        draw_board_player()
        pass
    elif option == "1 - BFS":
        algorithm = alg.bfs
        pass
    elif option == "2 - DFS":
        algorithm = alg.dfs
        pass
    elif option == "3 - IDS":
        algorithm = alg.ids
        pass
    elif option == "4 - Greedy":
        algorithm = alg.greedy_search
        pass
    elif option == "5 - A*":
        algorithm = alg.a_star
        pass
    draw_board(algorithm)

start_button.config(command=start_game)


def draw_board(algorithm):
    global board
    size = len(board)
    cell_size = 100
    canvas_width = size * cell_size 
    canvas_height = size * cell_size

    # Create the main window
    window = tk.Tk()
    window.title("Board")

    # Create a canvas for drawing the board
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()
    #message_label.config(text="The game is starting")
    def draw():
        canvas.delete("all")
        # Draw the cells
        for i in range(size):
            for j in range(size):
                x1 = j * cell_size + 5
                y1 = i * cell_size + 5
                x2 = x1 + cell_size - 10
                y2 = y1 + cell_size - 10
                color = board[i][j]
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                if color == 'R':
                    canvas.create_rectangle(x1+5, y1+5, x2-5, y2-5, fill="red")
                elif color == 'G':
                    canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="green")
                elif color == 'B':
                    canvas.create_polygon(
                        x1+5, y2-5, x2-5, y2-5, (x1+x2)//2, y1+5, fill="blue")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill='white')

    # Draw the initial board
    draw()

    # Create a label for messages
    message_label = tk.Label(window, text="", font=("Arial", 20), fg="black")
    message_label.pack()

    # Configure label's background color to transparent
    message_label.config(bg="SystemButtonFace")

    # Clear the message label
    board, visited = algorithm(board)
    message_label.config(text=f"Solution found after {visited} states")
    quit_button = tk.Button(window, text="Quit", command=window.destroy)
    quit_button.pack(side="left")

def draw_board_player():
    global board
    size = len(board)
    cell_size = 100
    canvas_width = size * cell_size 
    canvas_height = size * cell_size

    # Create the main window
    window = tk.Tk()
    window.title("Board")

    # Create a canvas for drawing the board
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

    def draw():
        canvas.delete("all")
        # Draw the cells
        for i in range(size):
            for j in range(size):
                x1 = j * cell_size + 5
                y1 = i * cell_size + 5
                x2 = x1 + cell_size - 10
                y2 = y1 + cell_size - 10
                color = board[i][j]
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                if color == 'R':
                    canvas.create_rectangle(x1+5, y1+5, x2-5, y2-5, fill="red")
                elif color == 'G':
                    canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="green")
                elif color == 'B':
                    canvas.create_polygon(
                        x1+5, y2-5, x2-5, y2-5, (x1+x2)//2, y1+5, fill="blue")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill='white')

    # Draw the initial board
    draw()

    # Create a label for messages
    message_label = tk.Label(window, text="", font=("Arial", 20), fg="black")
    message_label.pack()

    # Configure label's background color to transparent
    message_label.config(bg="SystemButtonFace")

    # Clear the message label
    message_label.config(text="")

    # Create row selector
    row_label = tk.Label(window, text="Row:")
    row_label.pack(side="left")
    row_entry = tk.Entry(window)
    row_entry.pack(side="left")
    
    # Create column selector
    col_label = tk.Label(window, text="Column:")
    col_label.pack(side="left")
    col_entry = tk.Entry(window)
    col_entry.pack(side="left")
    
    # Create color selector
    color_label = tk.Label(window, text="Color:")
    color_label.pack(side="left")
    color_var = tk.StringVar(window)
    color_var.set("R")  # Set default color to Red
    color_options = ["R", "G", "B"]
    color_menu = tk.OptionMenu(window, color_var, *color_options)
    color_menu.pack(side="left")
    print("loop")
    # Create submit button
    def submit():
        global board
        row = int(row_entry.get())
        col = int(col_entry.get())
        color = color_var.get()
        if(logic.verifyInCanPutPiece(board, row-1,col-1)):
            board = logic.putPieceInBoard(board, color, row-1, col-1)
        draw()
        if (logic.verifyGameEnd(board)):
            message_label.config(text="You win!")
            draw()
        if (logic.verifyGameEnd(board)):
            sleep(2)
        
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()
    quit_button = tk.Button(window, text="Quit", command=lambda root=window:quit(root)).pack()
    quit_button.pack(side="left")




    # Start the main event loop
    window.mainloop()


# Start the main event loop
window.mainloop()

def quit(root):
    root.destroy()