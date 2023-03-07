import tkinter as tk

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
algorithms = ["1 - BFS",
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


# Create a function to start the game when the button is clicked
def start_game():
    try:
        level = int(level_entry.get())
    except ValueError:
        level = 1 # default level if no input
    algorithm = algorithm_var.get()
    draw_board(5, [
        [' ', ' ', ' ', 'B', 'R'],
        [' ', ' ', ' ', 'R', ' '],
        ['G', 'G', 'G', ' ', 'G'],
        [' ', 'B', 'B', ' ', 'G'],
        [' ', ' ', 'R', ' ', ' ']
    ])
    # Code to start the game using the selected level and algorithm goes here
    pass


start_button.config(command=start_game)


def draw_board(X, board):
    cell_size = 50
    canvas_width = len(board[0]) * cell_size
    canvas_height = len(board) * cell_size

    # Create the main window
    window = tk.Tk()
    window.title("Board")

    # Create a canvas for drawing the board
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Draw the cells
    for i in range(len(board)):
        for j in range(len(board[0])):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = board[i][j]
            if color == 'R':
                fill_color = "red"
            elif color == 'G':
                fill_color = "green"
            elif color == 'B':
                fill_color = "blue"
            else:
                fill_color = "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

    # Create a label for the user input
    input_label = tk.Label(window, text="Enter color, row, and column:")
    input_label.pack()

    # Create entry widgets for color, row, and column
    color_entry = tk.Entry(window)
    row_entry = tk.Entry(window)
    col_entry = tk.Entry(window)

    # Grid layout for the entry widgets
    color_entry.grid(row=1, column=0)
    row_entry.grid(row=1, column=1)
    col_entry.grid(row=1, column=2)

    # Create a button for submitting the user input
    submit_button = tk.Button(window, text="Submit")
    submit_button.grid(row=2, column=1)

    # Create a label for messages
    message_label = tk.Label(window, text="")
    message_label.pack(side="bottom")

    # Function to handle button click event
    def submit():
        color = color_entry.get()
        row = int(row_entry.get()) - 1
        col = int(col_entry.get()) - 1

        # Check if the row and column are valid
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            message_label.config(text="Invalid row or column")
            return

        # Update the board
        board[row][col] = color
        if color == 'R':
            fill_color = "red"
        elif color == 'G':
            fill_color = "green"
        elif color == 'B':
            fill_color = "blue"
        else:
            fill_color = "white"
        canvas.itemconfig(len(board[0]) * row + col + 1, fill=fill_color)

        # Clear the message label
        message_label.config(text="")

    # Bind the button to the submit function
    submit_button.config(command=submit)

    # Start the main event loop
    window.mainloop()


# Start the main event loop
window.mainloop()
