from random import shuffle
from tkinter import *
from  tkinter import messagebox


FIRST_USER_SYMBOL = "x"
SECOND_USER_SYMBOL = "0"
current_player = FIRST_USER_SYMBOL
bg = "#FA8072" # Color of backgroud 
counter_1 = 0 # Counter of wins
counter_2 = 0 # Counter of wins 
counter = 0 # Counter of turns

# Root settings
root = Tk()
root.title("TicTactoe")
root.geometry("800x700+10+100")
root.config(bg=bg)
root.resizable(False, False)

# Frames
top_frame = Frame(bg=bg)
game_frame = Frame()
stat_frame = Frame(bg=bg)
statistic_frame = Frame(bg=bg)

# Frames.grid
top_frame.grid(column=0, row=0, columnspan=2, sticky="w")
game_frame.grid(column=0, row=2, sticky="w")
stat_frame.grid(column=1, row=1, sticky="ne")
statistic_frame.grid(column=0, row=8, sticky="ne")

def create_board():
    global game_board
    # Destroy widgets
    name_player_1.grid_forget()
    name_player_2.grid_forget()
    entry_1.grid_forget()
    entry_2.grid_forget()
    button_enter.grid_forget()

    current_player == FIRST_USER_SYMBOL # First turn - X
    
    # Creating new board
    size = 3 # Size of the board

    for elmnt in game_frame.grid_slaves():
        elmnt.grid_remove()

    game_board = [[Entry(game_frame,font=('Comic Sans MS', 35, 'bold',), width=2, justify=CENTER) for i in range(size)] for j in
                  range(size)]  # List comprehantions of the Entry
    # Input control of the board
    for row in range(size):
        for col in range(size):
            game_board[row][col].bind("<KeyRelease>", input_control)
            game_board[row][col].grid(column=col, row=row, ipadx=30, ipady=30, padx=5, pady=5, sticky='snew')

def remove_board():
    global current_player 
    # Board remove(with grid.forget)
    size = 3
    for row in range(size):
        for col in range(size):
            game_board[row][col].grid_forget()  
    error.grid_forget()
    turn.grid_forget()
    current_player = FIRST_USER_SYMBOL
    create_board()
    
def check_player_1():
    global name_of_player_1
    if len(entry_1.get()) == 0: # If name of player 1 is empty
        name_of_player_1 = "x" # Name player 1 is zero
    else:    
        name_of_player_1 = entry_1.get().title() # Get player 1 name

def check_player_2():
    global name_of_player_2
    if len(entry_2.get()) == 0: # If field name is empty
        name_of_player_2 = "0"
    else:    
        name_of_player_2 = entry_2.get().title() 

def input_control(event):
    global game_board, current_player, size, counter, counter_1, counter_2
    current_widget = event.widget  # Field
    error.config(text="", fg="black")
    field_value = current_widget.get()  # Get a value from a field now

    if field_value != current_player:  # If it is not my turn
        current_widget.delete(0, END)
        error.config(text="Wrong symbol/player", fg="black") # Alert
        return

    current_widget.config(state="disabled")  # Blocking free fields
    


    if check_winner():  # True / False

        for row in game_board:
            for e in row:
                # Blocking free fields
                e.config(state="disabled")  

        if current_player == 'x':
            check_player_1()
            messagebox.showinfo("Tic Tac Toe", f"Congratulations for {name_of_player_1}\nyou've won!") # Show a win
            counter_1 +=1
            # Check for win/wins
            if counter_1 == 1:
                counter_lbl_1.config(text=f"{name_of_player_1} has {counter_1} win")
            else:
                counter_lbl_1.config(text=f"{name_of_player_1} has {counter_1} wins")
            
            
        if current_player == "0":
            check_player_2()
            messagebox.showinfo("Tic Tac Toe", f"Congratulations for {name_of_player_2}\nyou've won!") # Show a win
            counter_2 +=1
            if counter_2 == 1:
                counter_lbl_2.config(text=f"{name_of_player_2} has {counter_2} win")
            else:
                counter_lbl_2.config(text=f"{name_of_player_2} has {counter_2} wins")
      
 
        remove_board()
        return
        
    
    # Check turns
    if current_player == FIRST_USER_SYMBOL: # If now x
        current_player = SECOND_USER_SYMBOL # Current player - 0
        check_player_2()
        turn.config(text=f"Turn of {name_of_player_2}", fg="black") 
        counter += 1 # Count of turns
    else:
        current_player = FIRST_USER_SYMBOL # Current_player - x
        check_player_1()
        turn.config(text=f"Turn of {name_of_player_1}", fg="black")
        counter += 1

    if counter == 9: #If game board is fully(Standoff)
        messagebox.showinfo("Tic Tac Toe", 'Standoff')
        remove_board()
    
def check_winner():
    
    for row in game_board:
        if row[0].get() == '': continue
        if len(set(map(lambda e: e.get(), row))) == 1: return True

    # Check column
    for column_number in range(len(game_board)):
        temp_list = [game_board[r][column_number].get() for r in range(len(game_board))]
        if temp_list.count(current_player) == len(game_board): return True

    # check diagonals
    temp_list = [game_board[i][i].get() for i in range(len(game_board))]
    if temp_list.count(current_player) == len(game_board):
        return True

    temp_list = [game_board[i][len(game_board) - 1 - i].get() for i in range(len(game_board))]
    if temp_list.count(current_player) == len(game_board):
        return True

    return False  # Winner not found

def create_game():
    # Entry for names players and button Enter
    name_player_1.grid(column=0, row=2)
    name_player_2.grid(column=0, row=3)

    entry_1.grid(row=2, column=1, pady=10, ipadx=5)
    entry_2.grid(row=3, column=1, ipadx=5)

    button_enter.grid(row=4, column=1, pady=5)

# Entry and Labels
name_label = Label(top_frame, text="TicTacToe", font=('Times New Roman', 25, 'bold'), bg=bg, fg='white')
name_owner = Label(top_frame, text="©Grigoriy Sokolov", font=('Times New Roman', 20, "bold"), bg=bg, fg='white')
name_player_1 = Label(top_frame, text="Player 1", font=('Times New Roman', 20, "bold"), bg=bg, fg='white')
name_player_2 = Label(top_frame, text="Player 2", font=('Times New Roman', 20, "bold"), bg=bg, fg='white')
entry_1 = Entry(top_frame)
entry_2 = Entry(top_frame)

# Buttons
new_game = Button(top_frame, text="New Game", font=('Times New Roman', 20), command=create_game)
button_enter = Button(top_frame, text="Enter", font=('Times New Roman', 15), command=create_board)
clear_board = Button(top_frame, text="Clear board", font=('Times New Roman', 20), command=remove_board)

# Errors and winner labels
error = Label(stat_frame, bg=bg, font=('Comic Sans MS', 25, 'bold',))
error.pack(padx=10)
winner = Label(stat_frame, bg=bg, font=('Comic Sans MS', 35, 'bold',))
winner.pack(anchor=W)
# Turn label
turn = Label(stat_frame, bg=bg, font=('Comic Sans MS', 30, 'bold',))
turn.pack(padx=100)
# Statistic label
counter_lbl_1 = Label(statistic_frame, bg=bg, font=('Comic Sans MS', 25, 'bold',)) 
counter_lbl_2 = Label(statistic_frame ,bg=bg, font=('Comic Sans MS', 25, 'bold',)) 
counter_lbl_1.grid()
counter_lbl_2.grid()
# Labels.grid
name_label.grid(column=0, row=0)
name_owner.grid(column=0, row=1, pady=5)
# Buttons.grid
new_game.grid(row=0, column=1, padx=10)
clear_board.grid(row=0, column=4, padx=10)



root.mainloop()



