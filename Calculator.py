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
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#2c3e50", fg="#ecf0f1", padx=24, font=("Arial", 18))
        total_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#2c3e50", fg="#ecf0f1", padx=24, font=("Arial", 32))
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
        self.bind('<KeyPress>', self.on_key_press)
        self.bind('<Return>', lambda event: self.evaluate())
        self.bind('<BackSpace>', lambda event: self.clear_entry())
        self.bind('<c>', lambda event: self.clear())
        self.bind('<percent>', lambda event: self.apply_function(lambda x: x / 100))
        self.bind('<q>', lambda event: self.quit())
        self.bind('<exclam>', lambda event: self.apply_function(math.factorial))  
        self.bind('<1>', lambda event: self.apply_function(lambda x: 1 / x))  
        self.bind('<d>', lambda event: self.apply_function(math.degrees)) 
        self.bind('<r>', lambda event: self.apply_function(math.radians))  

    def on_key_press(self, event):
        key = event.char
        if key in '0123456789.':
            self.append_value(key)
        elif key in '+-*/':
            self.append_operator(key)
        elif key == '\r':
            self.evaluate()
        elif key == '\x08':
            self.clear_entry()
        elif key == 'c' or key == 'C':
            self.clear()
        elif key == '%':
            self.apply_function(lambda x: x / 100)
        elif key == 'p':
            self.append_value(math.pi)
        elif key == '^':
            if event.keysym == '2':
                self.apply_function(lambda x: x ** 2)
            elif event.keysym == '3':
                self.apply_function(lambda x: x ** 3)
        elif key == 'r':
            self.apply_function(math.sqrt)
        elif key == 'l':
            self.apply_function(math.log10)
        elif key == 'e':
            self.apply_function(math.exp)
        elif key == 's':
            self.apply_function(math.sin)
        elif key == 'c':
            self.apply_function(math.cos)
        elif key == 't':
            self.apply_function(math.tan)
        elif key == 'm':
            self.memory += self.get_value()
        elif key == 'M':
            self.current_expression = str(self.memory)
        elif key == 'M' and event.keysym == 'minus':
            self.memory -= self.get_value()
        elif key == 'h':
            self.show_history()
        elif key == 'q':
            self.quit()
        elif key == '!':
            self.apply_function(math.factorial)
        elif key == '1':
            self.apply_function(lambda x: 1 / x)
        elif key == 'd':
            self.apply_function(math.degrees)
        elif key == 'r':
            self.apply_function(math.radians)

        self.update_display()

    def on_button_click(self, button):
        if button == 'C':
            self.clear()
        elif button == 'CE':
            self.clear_entry()
        elif button == '=':
            self.evaluate()
        elif button in ['+', '-', '*', '/']:
            self.append_operator(button)
        elif button == 'π':
            self.append_value(math.pi)
        elif button == '^2':
            self.apply_function(lambda x: x ** 2)
        elif button == '^3':
            self.apply_function(lambda x: x ** 3)
        elif button == '√':
            self.apply_function(math.sqrt)
        elif button == 'log':
            self.apply_function(math.log10)
        elif button == 'exp':
            self.apply_function(math.exp)
        elif button == 'sin':
            self.apply_function(math.sin)
        elif button == 'cos':
            self.apply_function(math.cos)
        elif button == 'tan':
            self.apply_function(math.tan)
        elif button == '%':
            self.apply_function(lambda x: x / 100)
        elif button == 'M+':
            self.memory += self.get_value()
        elif button == 'M-':
            self.memory -= self.get_value()
        elif button == 'MR':
            self.current_expression = str(self.memory)
        elif button == 'MC':
            self.memory = 0
        elif button == 'History':
            self.show_history()
        elif button == 'Quit':
            self.quit()
        elif button == '!':
            self.apply_function(math.factorial)
        elif button == '1/x':
            self.apply_function(lambda x: 1 / x)
        elif button == 'deg':
            self.apply_function(math.degrees)
        elif button == 'rad':
            self.apply_function(math.radians)
        elif button == 'sinh':
            self.apply_function(math.sinh)
        elif button == 'cosh':
            self.apply_function(math.cosh)
        elif button == 'tanh':
            self.apply_function(math.tanh)
        elif button == 'log2':
            self.apply_function(math.log2)
        elif button == 'bin':
            self.current_expression = bin(int(self.get_value()))
        elif button == 'oct':
            self.current_expression = oct(int(self.get_value()))
        elif button == 'hex':
            self.current_expression = hex(int(self.get_value()))
        elif button == 'dec':
            self.current_expression = str(int(self.current_expression, 0))
        elif button == 'Theme':
            self.change_theme()
        elif button == 'Save':
            self.save_history()
        elif button == 'Load':
            self.load_history()
        elif button == 'Clear Hist':
            self.clear_history()
        else:
            self.append_value(button)

        self.update_display()

    def apply_function(self, func):
        if self.current_expression != "":
            try:
                value = float(self.current_expression)
                self.current_expression = str(func(value))
                self.add_to_history(self.current_expression)
            except ValueError:
                self.current_expression = "Error"

    def append_value(self, value):
        self.current_expression += str(value)

    def append_operator(self, operator):
        if self.current_expression == "":
            return
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
        except Exception as e:
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
        messagebox.showinfo("Save History", "History save successfully!")

    def load_history(self):
        try:
            with open("history.txt", "r") as file:
                self.history = file.readlines()
            self.history = [entry.strip() for entry in self.history]
            messagebox.showinfo("Load History", "History loaded successfully!")
        except FileNotFoundError:
            messagebox.showerror("Load History", "No history file found.")

    def clear_history(self):
        self.history = []
        messagebox.showinfo("Clear History", "History cleared!")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
