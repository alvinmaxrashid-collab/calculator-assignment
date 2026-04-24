import tkinter as tk
import math

# Function to update the expression in the entry field
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

# Function to evaluate the expression
def evaluate():
    try:
        expression = entry.get()

        # Handle percentage by dividing the value by 100
        if "%" in expression:
            expression = expression.replace('%', '')
            result = float(expression) / 100
        else:
            result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field (All Clear)
def clear():
    entry.delete(0, tk.END)

# Function to delete the last character
def backspace():
    current = entry.get()
    entry.delete(len(current)-1, tk.END)

# Function for trigonometric and logarithmic functions
def scientific_function(func):
    try:
        expression = entry.get()
        if func == "sin":
            result = math.sin(math.radians(float(expression)))
        elif func == "cos":
            result = math.cos(math.radians(float(expression)))
        elif func == "tan":
            result = math.tan(math.radians(float(expression)))
        elif func == "log":
            result = math.log10(float(expression))
        elif func == "ln":
            result = math.log(float(expression))
        elif func == "sqrt":
            result = math.sqrt(float(expression))
        elif func == "sinh":
            result = math.sinh(math.radians(float(expression)))
        elif func == "cosh":
            result = math.cosh(math.radians(float(expression)))
        elif func == "tanh":
            result = math.tanh(math.radians(float(expression)))
        elif func == "factorial":
            result = math.factorial(int(expression))
        elif func == "pi":
            result = math.pi
        elif func == "mod":
            parts = expression.split("%")
            result = float(parts[0]) % float(parts[1])
        elif func == "exp":
            result = math.exp(float(expression))
        elif func == "power":
            parts = expression.split("^")
            result = float(parts[0]) ** float(parts[1])

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to convert between radians and degrees
def toggle_deg_rad():
    current = entry.get()
    if current:
        if "deg" in current:
            # If it's in "deg", convert to radians
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(math.radians(float(current.split('deg')[0]))))
        elif "rad" in current:
            # If it's in radians, convert to degrees
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(math.degrees(float(current.split('rad')[0]))))
        else:
            entry.insert(tk.END, "deg")

# Memory functions
memory = 0

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(memory))

def memory_store():
    global memory
    memory = float(entry.get())

def memory_add():
    global memory
    memory += float(entry.get())

def memory_subtract():
    global memory
    memory -= float(entry.get())

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")
window.config(bg="#2d2d2d")  # Dark background for a scientific theme

# Entry widget to display expressions and results
entry = tk.Entry(window, width=25, font=('Courier New', 16), borderwidth=3, relief="solid", bg="#1d1d1d", fg="#00ff00", justify="right")
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# Create buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4), ('deg', 1, 5),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4), ('rad', 2, 5),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4), ('^', 3, 5),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('sqrt', 4, 4), ('log', 4, 5),
    ('ln', 5, 0), ('(', 5, 1), (')', 5, 2), ('C', 5, 3), ('<', 5, 4),
    ('%', 6, 0), ('sinh', 6, 1), ('cosh', 6, 2), ('tanh', 6, 3), ('1/2', 6, 4), ('pi', 6, 5),
    ('mod', 7, 0), ('exp', 7, 1), ('10^x', 7, 2), ('n!', 7, 3), ('MC', 7, 4), ('MR', 7, 5),
    ('MS', 8, 0), ('M+', 8, 1), ('M-', 8, 2)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#00b300", fg="white", command=evaluate).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'C':
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#ff3333", fg="white", command=clear).grid(row=row, column=col, padx=5, pady=5)
    elif text == '<':
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#ffcc00", fg="black", command=backspace).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'MC':
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#333333", fg="white", command=memory_clear).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'MR':
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#333333", fg="white", command=memory_recall).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'MS':
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#333333", fg="white", command=memory_store).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'M+':
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#333333", fg="white", command=memory_add).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'M-':
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#333333", fg="white", command=memory_subtract).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(window, text=text, width=5, height=2, font=('Courier New', 14), bg="#333333", fg="white", command=lambda key=text: scientific_function(key) if key in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'sinh', 'cosh', 'tanh', 'mod', 'exp', 'pi', 'factorial', 'power'] else press(key)).grid(row=row, column=col, padx=5, pady=5)

# Run the main loop to display the window
window.mainloop()