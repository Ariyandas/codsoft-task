import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operation"
    
    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Ariyan Calculator")

entry_num1 = tk.Entry(root, width=10)
entry_num1.pack(pady=10)

entry_num2 = tk.Entry(root, width=10)
entry_num2.pack(pady=10)

operation_var = tk.StringVar()
operation_options = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(root, operation_var, *operation_options)
operation_menu.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

root.mainloop()