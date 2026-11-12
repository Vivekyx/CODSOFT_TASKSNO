import tkinter as tk
from tkinter import messagebox
import ast
import operator
import math

history = []

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg
}

def safe_calculate(expression):
    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        elif isinstance(node, ast.BinOp) and type(node.op) in operators:
            return operators[type(node.op)](
                evaluate(node.left), evaluate(node.right)
            )
        elif isinstance(node, ast.UnaryOp) and type(node.op) in operators:
            return operators[type(node.op)](evaluate(node.operand))
        else:
            raise ValueError("Invalid expression")

    return evaluate(ast.parse(expression, mode="eval").body)


def press(value):
    current = display_var.get()

    if current == "Error":
        current = ""

    if value == "C":
        display_var.set("")
    elif value == "⌫":
        display_var.set(current[:-1])
    elif value == "√":
        try:
            number = safe_calculate(current)
            if number < 0:
                raise ValueError
            result = math.sqrt(number)
            display_var.set(str(result))
        except Exception:
            display_var.set("Error")
    elif value == "x²":
        try:
            result = safe_calculate(current) ** 2
            display_var.set(str(result))
        except Exception:
            display_var.set("Error")
    elif value == "=":
        calculate()
    else:
        display_var.set(current + value)


def calculate():
    expression = display_var.get()

    try:
        result = safe_calculate(expression)

        if not math.isfinite(result):
            raise ValueError

        history.append(f"{expression} = {result}")
        history_list.insert(tk.END, history[-1])
        display_var.set(str(result))

    except ZeroDivisionError:
        display_var.set("Error")
        messagebox.showerror("Error", "Cannot divide by zero")

    except Exception:
        display_var.set("Error")
        messagebox.showerror("Error", "Invalid calculation")


def keyboard_input(event):
    key = event.char

    if key in "0123456789+-*/().%":
        press(key)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        press("⌫")
    elif event.keysym == "Escape":
        press("C")


window = tk.Tk()
window.title("Vivek's Professional Calculator")
window.geometry("550x650")
window.config(bg="#111827")
window.resizable(False, False)

display_var = tk.StringVar()

heading = tk.Label(
    window,
    text="VIVEK CALCULATOR",
    font=("Arial", 20, "bold"),
    bg="#111827",
    fg="#60a5fa"
)
heading.pack(pady=15)

display = tk.Entry(
    window,
    textvariable=display_var,
    font=("Arial", 25),
    justify="right",
    bd=0,
    bg="#1f2937",
    fg="white",
    insertbackground="white"
)
display.pack(fill="x", padx=20, ipady=15)

main_frame = tk.Frame(window, bg="#111827")
main_frame.pack(pady=20)

buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["√", "0", ".", "="],
    ["(", ")", "x²", "00"]
]

for row_index, row in enumerate(buttons):
    for col_index, value in enumerate(row):

        color = "#374151"

        if value in ["=", "+", "-", "*", "/"]:
            color = "#2563eb"
        elif value == "C":
            color = "#dc2626"

        button = tk.Button(
            main_frame,
            text=value,
            font=("Arial", 16, "bold"),
            width=7,
            height=2,
            bg=color,
            fg="white",
            activebackground="#60a5fa",
            activeforeground="white",
            bd=0,
            command=lambda v=value: press(v)
        )
        button.grid(
            row=row_index,
            column=col_index,
            padx=5,
            pady=5
        )

history_heading = tk.Label(
    window,
    text="Calculation History",
    font=("Arial", 13, "bold"),
    bg="#111827",
    fg="white"
)
history_heading.pack(pady=5)

history_list = tk.Listbox(
    window,
    height=5,
    font=("Arial", 10),
    bg="#1f2937",
    fg="white",
    bd=0
)
history_list.pack(fill="x", padx=20)

window.bind("<Key>", keyboard_input)
display.focus_set()

window.mainloop()