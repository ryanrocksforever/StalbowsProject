import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variables to track the game state
player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]

buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def on_click(row, col):
    global player
    if board[row][col] == '':
        board[row][col] = player
        buttons[row][col].config(text=player)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            root.quit()
        elif all(all(cell != '' for cell in row) for row in board):
            messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()
        player = 'O' if player == 'X' else 'X'

# Create the buttons
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text='', width=10, height=3, command=lambda r=row, c=col: on_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

root.mainloop()
