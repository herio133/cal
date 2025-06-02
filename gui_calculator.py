import tkinter as tk
from tkinter import messagebox

def calculate(choice, num1, num2):
    operations = {
        1: ('+', lambda x, y: x + y),
        2: ('-', lambda x, y: x - y),
        3: ('*', lambda x, y: x * y),
        4: ('/', lambda x, y: x / y if y != 0 else None)
    }

    op, func = operations.get(choice)
    if choice == 4 and num2 == 0:
        return None, "Error: Division by zero!"

    result = func(num1, num2)
    return f"{num1} {op} {num2}", result

class PandaCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panda Calculator 🐼")
        self.geometry("400x500")
        self.resizable(False, False)
        self.history = []

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Simple Calculator 🐼", font=("Arial", 20)).pack(pady=10)
        frame = tk.Frame(self)
        frame.pack(pady=5)

        tk.Label(frame, text="First number:").grid(row=0, column=0, pady=5, sticky="e")
        self.num1_entry = tk.Entry(frame)
        self.num1_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Second number:").grid(row=1, column=0, pady=5, sticky="e")
        self.num2_entry = tk.Entry(frame)
        self.num2_entry.grid(row=1, column=1, pady=5)

        # Operation buttons
        op_frame = tk.Frame(self)
        op_frame.pack(pady=10)
        tk.Button(op_frame, text="+", width=5, command=lambda: self.operate(1)).grid(row=0, column=0, padx=5)
        tk.Button(op_frame, text="-", width=5, command=lambda: self.operate(2)).grid(row=0, column=1, padx=5)
        tk.Button(op_frame, text="*", width=5, command=lambda: self.operate(3)).grid(row=0, column=2, padx=5)
        tk.Button(op_frame, text="/", width=5, command=lambda: self.operate(4)).grid(row=0, column=3, padx=5)

        # Result display
        self.result_label = tk.Label(self, text="", font=("Arial", 16), fg="blue")
        self.result_label.pack(pady=10)

        # History
        tk.Label(self, text="🐼 Calculation History:", font=("Arial", 12, "bold")).pack()
        self.history_box = tk.Listbox(self, width=40, height=10)
        self.history_box.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Clear", command=self.clear_fields).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Exit", command=self.quit).grid(row=0, column=1, padx=10)

    def operate(self, choice):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers.")
            return

        expr, res = calculate(choice, num1, num2)
        if expr is None:
            self.result_label.config(text=res, fg="red")
        else:
            self.result_label.config(text=f"Result: {expr} = {res}", fg="blue")
            self.history.append(f"{expr} = {res}")
            self.history_box.insert(tk.END, f"{expr} = {res}")

    def clear_fields(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    app = PandaCalculator()
    app.mainloop()