import tkinter as tk
import calculation

def main_window():
    global entry_guesses
    global top_frame
    global bottom_frame
    global lbl_bulls
    global lbl_cows
    global window
    global btn_check

    window = tk.Tk()
    window.title("Bulls and Cows game")

    # Create top frame
    top_frame = tk.Frame(window, width=400, height=200)
    top_frame.grid(row=0, column=0, sticky="nsew")

    # Create bottom frame
    bottom_frame = tk.Frame(window, width=400, height=50)
    bottom_frame.grid(row=1, column=0, sticky="nsew")

    # Configure row and column weights to make them resizable
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.columnconfigure(0, weight=1)

    # Contents in top frame
    lbl_game_title = tk.Label(top_frame, text="Bulls and Cows")
    lbl_game_title.grid(row=0, column=1, padx=10, pady=10)

    lbl_guess = tk.Label(top_frame, text="Your Guess")
    lbl_guess.grid(row=1, column=0, padx=10, pady=10)

    lbl_bulls = tk.Label(top_frame, text="Bull(s)")
    lbl_bulls.grid(row=1, column=1, padx=10, pady=10)

    lbl_cows = tk.Label(top_frame, text="Cow(s)")
    lbl_cows.grid(row=1, column=2, padx=10, pady=10)

    entry_guesses = []  # List to store references to entry widgets

    # Content in bottom_frame
    btn_check = tk.Button(bottom_frame, text="Start", command=generate_num)
    btn_check.grid(row=0, column=0, padx=10, pady=10)

    window.mainloop()

def generate_num():
    global actual_num
    global ent_num_entries
    global bull_labels
    global cow_labels
    global count
    global row_counter
    global entry_guesses
    global top_frame
    global btn_check

    actual_num = calculation.generate_rand_num()  # Generate random number
    btn_check["text"] = "Check"  # Change the text on the button
    btn_check.configure(command=add_entry)
    
    # Create a text box for user input
    entry_guess = tk.Entry(top_frame)
    entry_guess.grid(row=2, column=0, padx=10, pady=10)
    entry_guesses.append(entry_guess)  # Store a reference to the entry widget

    # Create a new entry for each guess
    ent_num_entries = []
    bull_labels = []
    cow_labels = []
    count = 0  # to keep track of inserted entries
    row_counter = 2
    # Create a new entry for each guess

def add_entry():
    global count
    global row_counter
    global actual_num
    global lbl_bulls
    global lbl_cows
    
    if count < 3:  # Limiting the number of guesses to 10
        if entry_guesses:  # Check if the list is not empty
            user_input = entry_guesses[-1].get()  # Get user's input from the entry
            bull_count, cow_count = calculation.check_num(user_input, actual_num)  # Check user input
            
            # Create labels for bull and cow count
            bull_label = tk.Label(top_frame, text=f"{bull_count}")
            bull_label.grid(row=row_counter, column=1, padx=10, pady=10)
            bull_labels.append(bull_label)
            
            cow_label = tk.Label(top_frame, text=f"{cow_count}")
            cow_label.grid(row=row_counter, column=2, padx=10, pady=10)
            cow_labels.append(cow_label)
            
            if bull_count == 4 and cow_count == 0:  # User guessed the correct number
                show_success_message()
                return  # Exit the function to prevent further processing
        
        if count < 2:  # Only add new entry if user has not reached maximum guesses
            entry_guess = tk.Entry(top_frame)
            entry_guess.grid(row=row_counter + 1, column=0, padx=10, pady=10)  # Grid the new entry
            entry_guesses.append(entry_guess)  # Store a reference to the entry widget
            count += 1
            row_counter += 1
        else:
            show_failure_message()    
    else:
        show_failure_message()

def show_success_message():
    global window

    success_window = tk.Toplevel(window)
    success_window.title("Success!")
    success_label = tk.Label(success_window, text="You guessed the correct number", padx=20, pady=20)
    success_label.pack()
    ok_button = tk.Button(success_window, text="Play Again", command=reset_game)
    ok_button.pack()

def show_failure_message():
    global window

    failure_window = tk.Toplevel(window)
    failure_window.title("Try Again")
    failure_label = tk.Label(failure_window, text="Oops...Try again", padx=20, pady=20)
    failure_label.pack()
    again_button = tk.Button(failure_window, text="Try Again", command=lambda: reset_game(failure_window))
    again_button.pack()

def reset_game(failure_window=None):
    global count
    global row_counter
    global btn_check
    global bull_label
    global cow_label
    global entry_guesses
    global bull_labels
    global cow_labels

    count = 0
    row_counter = 2
    for entry in ent_num_entries:
        entry.destroy()
    ent_num_entries.clear()
    for bull_label in bull_labels:
        bull_label.destroy()
    bull_labels.clear()
    for cow_label in cow_labels:
        cow_label.destroy()
    cow_labels.clear()
    for entry_guess in entry_guesses:  # Destroy the entry widgets
        entry_guess.destroy()
    entry_guesses.clear()
    lbl_bulls.config(text="Bull(s)")
    lbl_cows.config(text="Cow(s)")
    btn_check["text"] = "Start"
    btn_check.configure(command=generate_num)
    if failure_window:
        failure_window.destroy()