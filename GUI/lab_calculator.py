from tkinter import *
from tkinter import messagebox


start = Tk()
start.title("Calculator")

operator = IntVar()

left_entry = Entry(start) 
left_entry.grid(row=0, column=0, rowspan=4)

addition = Radiobutton(start, text="+", variable=operator, value=0)
addition.grid(row=0, column=1)

subtraction = Radiobutton(start, text="-", variable=operator, value=1)
subtraction.grid(row=1, column=1)

multiply = Radiobutton(start, text="x", variable=operator, value=2)
multiply.grid(row=2, column=1)

division = Radiobutton(start, text="/", variable=operator, value=3)
division.grid(row=3, column=1)

right_entry = Entry(start) 
right_entry.grid(row=0, column=2, rowspan=4)

def evaluate():
    num1 = left_entry.get()
    num2 = right_entry.get()
    op = operator.get()

    if not num1 or not num2:
        return messagebox.showinfo("Error", "Error issue")     
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return messagebox.showinfo("Error", "Error issue")
    

    result = 0

    if op == 0:
        result = num1 + num2
    elif op == 1:
        result = num1 - num2
    elif op == 2:
        result = num1 * num2
    elif op == 3:
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return messagebox.showinfo("Error", "Error issue")
    
        

    messagebox.showinfo("Result", f"{result}")     
    

    print("SOLVED")

solution = Button(start, text="Evaluate", command=evaluate)
solution.grid(row=4, column=0, columnspan=3)


start.mainloop()