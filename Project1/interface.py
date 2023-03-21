import tkinter as tk

import test_logic as logic

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
              "4 - UCS",
              "5 - Greedy",
              "6 - A*",
              "7 - Weighted A*",
              "8 - Manhattan Distance"]


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
board = [[' ', ' ', ' ', 'B', 'R'],
        [' ', 'B', 'B', ' ', 'B'],
        ['G', 'G', 'G', ' ', 'G'],
        [' ', 'B', 'B', ' ', 'G'],
        [' ', ' ', 'R', ' ', ' ']]


# Create a function to start the game when the button is clicked
def start_game():
    try:
        level = int(level_entry.get())
    except ValueError:
        level = 1  # default level if no input
    algorithm = algorithm_var.get()
    draw_board("The game is starting...")
    # Code to start the game using the selected level and algorithm goes here
    pass


start_button.config(command=start_game)


def draw_board(state):
    global board
    size = len(board)
    cell_size = 50*2
    canvas_width = size * cell_size 
    canvas_height = size * cell_size

    # Create the main window
    window = tk.Tk()
    window.title("Board")

    # Create a canvas for drawing the board
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

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

    # Create a label for messages
    message_label = tk.Label(window, text="", font=("Arial", 20), fg="black")
    message_label.pack()

    # Configure label's background color to transparent
    message_label.config(bg="SystemButtonFace")

    # Clear the message label
    message_label.config(text=state)

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
    color_var.set("Red")  # Set default color to Red
    color_options = ["Red", "Green", "Blue"]
    color_menu = tk.OptionMenu(window, color_var, *color_options)
    color_menu.pack(side="left")

    # Create submit button
    def submit():
        global board
        row = int(row_entry.get())
        col = int(col_entry.get())
        color = color_var.get()
        board = logic.putPieceInBoard(board, color, row, col)
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()




    # Start the main event loop
    window.mainloop()


# Start the main event loop
window.mainloop()