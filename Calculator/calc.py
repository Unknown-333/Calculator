import tkinter as tk

app = tk.Tk()
app.title("Calculator")

def on_button_click(event):
    current_text = display_var.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif button_text == "C":
        display_var.set("")
    else:
        display_var.set(current_text + button_text)    

display_var = tk.StringVar()
display_var.set("")

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

display = tk.Entry(app, textvar=display_var, font=("Times New Roman", 25))
display.grid(row=0, column=0, columnspan=len(buttons[0]), sticky="nsew")

for row, button_row in enumerate(buttons):
    for col, button_text in enumerate(button_row):
        button = tk.Button(app, text=button_text, font=("Times New Roman", 25))
        button.grid(row=row + 1, column=col, sticky="nsew")
        button.bind("<Button-1>", on_button_click)

# Make all rows and columns expandable
for i in range(len(buttons) + 1):
    app.grid_rowconfigure(i, weight=1)
for i in range(len(buttons[0])):
    app.grid_columnconfigure(i, weight=1)

app.mainloop()

