import tkinter as tk

window = tk.Tk()
window.title("Bulls and Cows game")

# Create top frame
top_frame = tk.Frame(window, width=400, height=200)
top_frame.grid(row = 0, column = 0, sticky = "nsew")

# Create bottom frame
bottom_frame = tk.Frame(window, width=400, height=50)
bottom_frame.grid(row = 1, column = 0, sticky = "nsew")

# Configure row and column weights to make them resizable
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.columnconfigure(0, weight = 1)

# Contents in top frame
lbl_game_title = tk.Label(top_frame, text = "Bulls and Cows")
lbl_game_title.grid(row=0, column=1, padx=10, pady=10)

lbl_guess = tk.Label(top_frame, text = "Your Guess")
lbl_guess.grid(row=1, column=0, padx=10, pady=10)

lbl_bulls = tk.Label(top_frame, text = "Bull(s)")
lbl_bulls.grid(row=1, column=1, padx=10, pady=10)

lbl_cows = tk.Label(top_frame, text = "Cow(s)")
lbl_cows.grid(row=1, column=2, padx=10, pady=10)

# 4-digit number generation upon clicking on 'Start' 
def generate_num():
    btn_check["text"] = "Check" # Change the text on the button
    btn_check.configure(command = add_entry)
    add_entry()

# Create a new entry for each guess
ent_num_entries = []
count = 0 # to keep track of inserted entries
row_counter = 3
def add_entry():
    global count
    global row_counter
    MAX_NUM = 9 #maximum numbers of entries - 1 
    if count <= MAX_NUM:
        ent_num_entries.append(tk.Entry(top_frame))
        ent_num_entries[-1].grid(row = row_counter, column = 0)
        count +=1
        row_counter +=1

# Content in bottom_frame
btn_check = tk.Button(bottom_frame, text = "Start", command = generate_num)
btn_check.grid(row=0, column=0, padx=10, pady=10)

window.mainloop()