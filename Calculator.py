import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Responsive Calculator")
        self.geometry("350x600")
        self.resizable(False, False)

        self.expression = ""
        self.memory = 0
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        self.display_frame = tk.Frame(self, bg="#2c3e50")
        self.display_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.total_expression = ""
        self.current_expression = ""

        self.total_label, self.label = self.create_display_labels()

        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

        self.create_buttons()

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        for i in range(10):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)

        self.bind_keys()

    def create_display_labels(self):
        total_label = tk.Label(
            self.display_frame, text=self.total_expression, anchor=tk.E,
            bg="#2c3e50", fg="#ecf0f1", padx=24, font=("Arial", 18)
        )
        total_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        label = tk.Label(
            self.display_frame, text=self.current_expression, anchor=tk.E,
            bg="#2c3e50", fg="#ecf0f1", padx=24, font=("Arial", 32)
        )
        label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        return total_label, label

    def create_buttons(self):
        button_colors = {
            'default': '#34495e',
            'highlight': '#e74c3c',
            'text': '#ecf0f1'
        }

        buttons = [
            ['C', 'CE', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', 'π'],
            ['^2', '^3', '√', 'log'],
            ['sin', 'cos', 'tan', 'exp'],
            ['M+', 'M-', 'MR', 'MC'],
            ['!', '1/x', 'deg', 'rad'],
            ['History', 'Quit'],
            ['sinh', 'cosh', 'tanh', 'log2'],
            ['bin', 'oct', 'hex', 'dec'],
            ['Theme', 'Save', 'Load', 'Clear Hist']
        ]

        for r, row in enumerate(buttons):
            for c, button in enumerate(row):
                button_obj = tk.Button(
                    self.button_frame,
                    text=button,
                    font=("Arial", 14),
                    borderwidth=0,
                    bg=button_colors['default'],
                    fg=button_colors['text'],
                    activebackground=button_colors['highlight'],
                    command=lambda x=button: self.on_button_click(x)
                )
                button_obj.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)

    def bind_keys(self):
        key_bindings = {
            '<Return>': self.evaluate,
            '<BackSpace>': self.clear_entry,
            '<c>': self.clear,
            '<percent>': lambda event: self.apply_function(lambda x: x / 100),
            '<q>': self.quit,
            '<exclam>': lambda event: self.apply_function(math.factorial),
            '<1>': lambda event: self.apply_function(lambda x: 1 / x),
            '<d>': lambda event: self.apply_function(math.degrees),
            '<r>': lambda event: self.apply_function(math.radians)
        }
        
        for key, handler in key_bindings.items():
            self.bind(key, handler)
        
        self.bind('<KeyPress>', self.on_key_press)

    def on_key_press(self, event):
        key = event.char
        key_actions = {
            '0123456789.': self.append_value,
            '+-*/': self.append_operator,
            '\r': self.evaluate,
            '\x08': self.clear_entry,
            'cC': self.clear,
            '%': lambda: self.apply_function(lambda x: x / 100),
            'p': lambda: self.append_value(math.pi),
            '^': lambda e: self.apply_function(lambda x: x ** 2 if e.keysym == '2' else x ** 3),
            'r': lambda: self.apply_function(math.sqrt),
            'l': lambda: self.apply_function(math.log10),
            'e': lambda: self.apply_function(math.exp),
            's': lambda: self.apply_function(math.sin),
            'c': lambda: self.apply_function(math.cos),
            't': lambda: self.apply_function(math.tan),
            'm': lambda: self.memory_add(self.get_value()),
            'M': lambda: self.memory_set(),
            'h': self.show_history,
            'q': self.quit,
            '!': lambda: self.apply_function(math.factorial),
            '1': lambda: self.apply_function(lambda x: 1 / x),
            'd': lambda: self.apply_function(math.degrees),
            'r': lambda: self.apply_function(math.radians)
        }

        for key_group, action in key_actions.items():
            if key in key_group:
                action(event)
                self.update_display()
                break

    def on_button_click(self, button):
        button_actions = {
            'C': self.clear,
            'CE': self.clear_entry,
            '=': self.evaluate,
            '+-*/': self.append_operator,
            'π': lambda: self.append_value(math.pi),
            '^2': lambda: self.apply_function(lambda x: x ** 2),
            '^3': lambda: self.apply_function(lambda x: x ** 3),
            '√': lambda: self.apply_function(math.sqrt),
            'log': lambda: self.apply_function(math.log10),
            'exp': lambda: self.apply_function(math.exp),
            'sin': lambda: self.apply_function(math.sin),
            'cos': lambda: self.apply_function(math.cos),
            'tan': lambda: self.apply_function(math.tan),
            '%': lambda: self.apply_function(lambda x: x / 100),
            'M+': lambda: self.memory_add(self.get_value()),
            'M-': lambda: self.memory_subtract(self.get_value()),
            'MR': lambda: self.current_expression = str(self.memory),
            'MC': lambda: self.memory_clear(),
            'History': self.show_history,
            'Quit': self.quit,
            '!': lambda: self.apply_function(math.factorial),
            '1/x': lambda: self.apply_function(lambda x: 1 / x),
            'deg': lambda: self.apply_function(math.degrees),
            'rad': lambda: self.apply_function(math.radians),
            'sinh': lambda: self.apply_function(math.sinh),
            'cosh': lambda: self.apply_function(math.cosh),
            'tanh': lambda: self.apply_function(math.tanh),
            'log2': lambda: self.apply_function(math.log2),
            'bin': lambda: self.current_expression = bin(int(self.get_value())),
            'oct': lambda: self.current_expression = oct(int(self.get_value())),
            'hex': lambda: self.current_expression = hex(int(self.get_value())),
            'dec': lambda: self.current_expression = str(int(self.current_expression, 0)),
            'Theme': self.change_theme,
            'Save': self.save_history,
            'Load': self.load_history,
            'Clear Hist': self.clear_history
        }

        if button in button_actions:
            button_actions[button]()
        else:
            self.append_value(button)

        self.update_display()

    def apply_function(self, func):
        if self.current_expression:
            try:
                value = float(self.current_expression)
                self.current_expression = str(func(value))
                self.add_to_history(self.current_expression)
            except ValueError:
                self.current_expression = "Error"

    def append_value(self, value):
        self.current_expression += str(value)

    def append_operator(self, operator):
        if self.current_expression:
            self.total_expression += self.current_expression + operator
            self.current_expression = ""

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.add_to_history("Cleared")

    def clear_entry(self):
        self.current_expression = ""

    def evaluate(self):
        self.total_expression += self.current_expression
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
            self.add_to_history(self.current_expression)
        except Exception:
            self.current_expression = "Error"
            self.add_to_history("Error")

    def get_value(self):
        try:
            return float(self.current_expression)
        except ValueError:
            return 0

    def add_to_history(self, entry):
        self.history.append(entry)
        if len(self.history) > 10:
            self.history.pop(0)

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("History")
        history_window.geometry("300x400")

        history_list = tk.Listbox(history_window)
        history_list.pack(expand=True, fill="both")

        for entry in self.history:
            history_list.insert(tk.END, entry)

    def update_display(self):
        self.total_label.config(text=self.total_expression)
        self.label.config(text=self.current_expression)

    def change_theme(self):
        themes = [
            {"bg": "#2c3e50", "fg": "#ecf0f1"},
            {"bg": "#ecf0f1", "fg": "#2c3e50"},
            {"bg": "#34495e", "fg": "#e74c3c"}
        ]
        current_theme = themes.pop(0)
        themes.append(current_theme)
        self.configure(bg=current_theme["bg"])
        self.display_frame.configure(bg=current_theme["bg"])
        self.total_label.configure(bg=current_theme["bg"], fg=current_theme["fg"])
        self.label.configure(bg=current_theme["bg"], fg=current_theme["fg"])

    def save_history(self):
        with open("history.txt", "w") as file:
            for entry in self.history:
                file.write(f"{entry}\n")
        messagebox.showinfo("Save History", "History saved successfully!")

    def load_history(self):
        try:
            with open("history.txt", "r") as file:
                self.history = [line.strip() for line in file]
            messagebox.showinfo("Load History", "History loaded successfully!")
        except FileNotFoundError:
            messagebox.showerror("Load History", "No history file found.")

    def clear_history(self):
        self.history = []
        messagebox.showinfo("Clear History", "History cleared!")

    def memory_add(self, value):
        self.memory += value

    def memory_subtract(self, value):
        self.memory -= value

    def memory_set(self):
        self.current_expression = str(self.memory)

    def memory_clear(self):
        self.memory = 0

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
