import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.configure(bg='#f0f0f0')  # Set background color

# Entry widget to display input and output
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 12))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Colors for buttons
button_colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9BF6FF']

# Create and place buttons on the grid
row = 1
col = 0
for idx, button in enumerate(buttons):
    if button == '=':
        tk.Button(root, text=button, padx=40, pady=20, bg=button_colors[3], fg='white', font=('Arial', 12, 'bold'), command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, padx=40, pady=20, bg=button_colors[1], fg='white', font=('Arial', 12, 'bold'), command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=40, pady=20, bg=button_colors[idx // 4], fg='black', font=('Arial', 12, 'bold'), command=lambda value=button: click_button(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()