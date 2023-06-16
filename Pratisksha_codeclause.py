import random
import string
import tkinter as tk
from tkinter import font, messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, password)
        
        # Password strength suggestion
        if length < 8:
            strength_label.config(text="Weak Password", fg="#FF0000")
        else:
            strength_label.config(text="Strong Password", fg="#00FF00")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid password length.")

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("800x600")
window.configure(bg="#ECEFF1")


# Make the window full screen
window.attributes('-fullscreen', True)

# Styling
label_font = font.Font(family="Times New Roman", size=25, weight="bold")

label_font1 = font.Font(family="Times New Roman", size=18, weight="bold")

entry_font = font.Font(family="Times New Roman", size=16)
button_font = font.Font(family="Times New Roman", size=16, weight="bold")

# Define the functions for minimize, maximize, and close buttons
def minimize_window():
    window.iconify()

def maximize_window():
    if window.attributes('-zoomed'):
        window.attributes('-zoomed', False)
    else:
        window.attributes('-zoomed', True)

def close_window():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        window.destroy()

# Create the title bar
title_bar = tk.Frame(window, bg="#455A64", relief=tk.RAISED, bd=0) 
title_bar.pack(side=tk.TOP, fill=tk.X)

# Create the close button
close_button = tk.Button(title_bar, text="\u2716", font=button_font, bg="#FF0000", fg="#FFFFFF",
                         activebackground="#FF0000", activeforeground="#FFFFFF",
                         bd=0, relief=tk.FLAT, command=close_window)
close_button.pack(side=tk.RIGHT, padx=5, pady=2)

# Create the maximize button
maximize_button = tk.Button(title_bar, text="\u25A1", font=button_font, bg="#455A64", fg="#FFFFFF",
                            activebackground="#37474F", activeforeground="#FFFFFF",
                            bd=0, relief=tk.FLAT, command=maximize_window)
maximize_button.pack(side=tk.RIGHT, padx=5, pady=2)

# Create the minimize button
minimize_button = tk.Button(title_bar, text="\u2212", font=button_font, bg="#455A64", fg="#FFFFFF",
                            activebackground="#37474F", activeforeground="#FFFFFF",
                            bd=0, relief=tk.FLAT, command=minimize_window)
minimize_button.pack(side=tk.RIGHT, padx=5, pady=2)

# Create the title label
title_label = tk.Label(window, text="Random Password Generator", font=label_font, bg="#ECEFF1", fg="#455A64")
title_label.pack(pady=50)

# Create the length label and entry
length_label = tk.Label(window, text="Password Length:", font=label_font1, bg="#ECEFF1", fg="#455A64")
length_label.pack()
length_entry = tk.Entry(window, font=entry_font, bd=1, relief=tk.SOLID)
length_entry.pack(pady=10)

# Create the generate button
generate_button = tk.Button(window, text="Generate Password", font=button_font, bg="#b30059", fg="#FFFFFF",
                            activeforeground="#FFFFFF", command=generate_button_click)
generate_button.pack(pady=10)

# Create the password entry
password_entry = tk.Entry(window, font=entry_font, bd=1, relief=tk.SOLID)
password_entry.pack(pady=10)

# Create the password strength label
strength_label = tk.Label(window, text="", font=label_font, bg="#ECEFF1")
strength_label.pack(pady=10)

# Start the main event loop
window.mainloop()




















