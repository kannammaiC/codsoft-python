import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Inputs
tk.Label(root, text="First Number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Operation (+ - * /)").grid(row=2, column=0)
operation = tk.Entry(root)
operation.grid(row=2, column=1)

# Calculate Button
calc_btn = tk.Button(root, text="Calculate", command=calculate)
calc_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()