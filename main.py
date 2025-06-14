import tkinter as tk

# Define calculator options

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == 'add':
            result.set(num1 + num2)
        elif operation == 'subtract':
            result.set(num1 - num2)
        elif operation == 'multiply':
            result.set(num1 * num2)
        elif operation == 'divide':
            if num2 == 0:
                result.set("Error: Divison by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid input")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")


# Set GUI Window
window = tk.Tk()
window.title("Simple Calculator")


# Input fields
tk.Label(window, text="First number:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Second number:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Result display
result = tk.StringVar()
tk.Label(window, text="Result:").grid(row=2, column=0, padx=5, pady=5)
tk.Label(window, textvariable=result).grid(row=2, column=1, padx=5, pady=5)

# Operation buttons
tk.Button(window, text="Add", command=lambda: calculate('add')).grid(row=3, column=0, padx=5, pady=5)
tk.Button(window, text="Subtract", command=lambda: calculate('subtract')).grid(row=3, column=1, padx=5, pady=5)
tk.Button(window, text="Multiply", command=lambda: calculate('multiply')).grid(row=4, column=0, padx=5, pady=5)
tk.Button(window, text="Divide", command=lambda: calculate('divide')).grid(row=4, column=1, padx=5, pady=5)

# Clear button
tk.Button(window, text="Clear", command=clear).grid(row=5, column=0, columnspan=2, pady=10)

# Run the app
window.mainloop()