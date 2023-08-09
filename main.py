import tkinter as tk


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.config(bg='gray')

        self.equation = tk.StringVar()
        self.entry_value = ""

        entry = tk.Entry(master, width=20, bg='#fff',
                         font=('Arial Bold', 28),
                         textvariable=self.equation)
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+', 'C'
        ]

        row = 1
        col = 0

        for btn_text in buttons:
            button = tk.Button(master, text=btn_text, width=10, height=3,
                               relief='flat', bg='white',
                               command=lambda
                               text=btn_text: self.on_button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

        master.bind('<Return>', lambda event: self.solve())

    def on_button_click(self, value):
        if value == 'C':
            self.clear()
        elif value == '=':
            self.solve()
        else:
            self.entry_value += str(value)
            self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.entry_value = str(result)
            self.equation.set(self.entry_value)
        except Exception:
            self.equation.set("Error")


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
