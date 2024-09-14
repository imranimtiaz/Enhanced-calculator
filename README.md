### Calculator Program Documentation

#### Overview
The calculator program supports a wide range of mathematical operations, including basic arithmetic, trigonometric functions, logarithmic functions, statistical calculations, and more. It also supports solving linear and quadratic equations, converting between degrees and radians, and matrix operations.

#### Features
- **Basic Arithmetic**: Addition, subtraction, multiplication, division, and exponentiation.
- **Square Root Calculation**: `sqrt` for square root.
- **Trigonometric Functions**: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`.
- **Logarithmic Functions**: `log` for natural logarithm, `log10` for base-10 logarithm.
- **Factorial Calculation**: `factorial` for calculating the factorial of an integer.
- **Modulo Operation**: `mod` for modulo operation.
- **Prime Check**: `prime` for checking if a number is prime.
- **Linear Equation Solving**: `eq` for solving linear equations of the form `ax + b = 0`.
- **Quadratic Equation Solving**: `qeq` for solving quadratic equations of the form `ax^2 + bx + c = 0`.
- **Degree-Radian Conversion**: `deg2rad` and `rad2deg`.
- **Statistical Calculations**: Mean (`mean`), median (`median`), mode (`mode`), standard deviation (`stddev`).
- **Matrix Operations**: `matrix` (not implemented yet).
- **Memory Operations**: `mem` for saving and recalling values from memory.

#### Usage
##### Main Menu
- The program displays a menu with available operations.
- Enter the corresponding operation keyword or symbol to perform a specific operation.
- To exit the program, type `exit`.

##### Basic Arithmetic and Expressions
- Supports expressions involving addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`^`).
- Expressions can be entered directly and will be evaluated.

##### Square Root
- Operation: `sqrt`
- Enter a number to calculate its square root.

##### Trigonometric Functions
- Operations: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
- Enter the angle in radians to calculate the corresponding trigonometric value.

##### Logarithmic Functions
- Operations: `log` (natural logarithm), `log10` (base-10 logarithm)
- Enter a number to calculate its logarithm.

##### Factorial Calculation
- Operation: `factorial`
- Enter an integer to calculate its factorial.

##### Modulo Operation
- Operation: `mod`
- Enter two integers to calculate the modulo (remainder) of their division.

##### Prime Check
- Operation: `prime`
- Enter an integer to check if it is a prime number.

##### Linear Equation Solving
- Operation: `eq`
- Enter the coefficients `a` and `b` for the linear equation `ax + b = 0` to find the value of `x`.

##### Quadratic Equation Solving
- Operation: `qeq`
- Enter the coefficients `a`, `b`, and `c` for the quadratic equation `ax^2 + bx + c = 0` to find the roots.

##### Degree-Radian Conversion
- Operations: `deg2rad`, `rad2deg`
- Convert degrees to radians or radians to degrees by entering the value.

##### Statistical Calculations
- Operations: `mean`, `median`, `mode`, `stddev`
- Enter the number of elements and their values to calculate the respective statistical measure.

##### Matrix Operations
- Operation: `matrix`
- Matrix operations are not yet implemented.

##### Memory Operations
- Operation: `mem`
- Save a value to memory or recall a value from memory.

#### Example Usage
##### Basic Arithmetic
```
> 3 + 4 * 2 / (1 - 5) ^ 2
Result: 3.50
```

##### Trigonometric Function
```
> sin
Enter the angle (in radians): 1.5708
Result: 1.00
```

##### Logarithmic Function
```
> log
Enter a number: 2.7183
Result: 1.00
```

##### Factorial
```
> factorial
Enter an integer: 5
Result: 120.00
```

##### Modulo Operation
```
> mod
Enter two integers: 10 3
Result: 1.00
```

##### Prime Check
```
> prime
Enter an integer: 7
Result: 7 is a prime number.
```

##### Linear Equation
```
> eq
Enter coefficients a and b for ax + b = 0: 2 -4
Result: 2.00
```

##### Quadratic Equation
```
> qeq
Enter coefficients a, b, and c for ax^2 + bx + c = 0: 1 -3 2
Roots: 2.00 and 1.00
```

##### Degree-Radian Conversion
```
> deg2rad
Enter degrees: 180
Radians: 3.14
```

### Notes
- The program handles both floating-point and integer inputs.
- Error messages are displayed for invalid operations or inputs, such as division by zero or invalid function names.
- Memory operations allow for saving and recalling values for later use.

---

### Python Docstrings

```python
import tkinter as tk
import math
from tkinter import messagebox

class Calculator(tk.Tk):
    """A class to represent a GUI calculator using Tkinter."""

    def __init__(self):
        """Initialize the calculator's GUI components and properties."""
        super().__init__()

        self.title("Responsive Calculator")
        self.geometry("350x600")
        self.resizable(False, False)

        self.expression = ""
        self.memory = 0
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the calculator's display and buttons."""
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

        for i in range(10):  # Updated to reflect the number of button rows
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)

        self.bind_keys()

    def create_display_labels(self):
        """Create the labels for displaying expressions and results."""
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#2c3e50", fg="#ecf0f1", padx=24, font=("Arial", 18))
        total_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#2c3e50", fg="#ecf0f1", padx=24, font=("Arial", 32))
        label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        return total_label, label

    def create_buttons(self):
        """Create the calculator's buttons."""
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
            ['History', 'Quit']
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
        """Bind keyboard keys to calculator actions."""
        self.bind('<KeyPress>', self.on_key_press)
        self.bind('<Return>', lambda event: self.evaluate())
        self.bind('<BackSpace>', lambda event: self.clear_entry())
        self.bind('<c>', lambda event: self.clear())
        self.bind('<percent>', lambda event: self.apply_function(lambda x: x / 100))
        self.bind('<q>', lambda event: self.quit())
        self.bind('<exclam>', lambda event: self.apply_function(math.factorial))  
        self.bind('<1>', lambda event: self

# Enhanced-calculator
