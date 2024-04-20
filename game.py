import tkinter as tk

window = tk.Tk()
window.title("Bulls and Cows game")
#for adjusting the grid as the window is resized
window.rowconfigure([0,1], weight = 1, minsize = 10)
window.columnconfigure([0,1,2,3,4], weight = 1, minsize = 10)

lbl_game_title = tk.Label(text = "Bulls and Cows")
lbl_game_title.grid(row = 0, column =2)

lbl_guess = tk.Label(text = "Your Guess")
lbl_guess.grid(row = 2, column = 1)

lbl_guess = tk.Label(text = "Bull(s)")
lbl_guess.grid(row = 2, column = 2)

lbl_guess = tk.Label(text = "Cow(s)")
lbl_guess.grid(row = 2, column = 3)

window.mainloop()