import tkinter as tk

def on_focus_in(event):
    print("Entry gained focus")

def on_focus_out(event):
    print("Entry lost focus")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack(padx=20, pady=20)

entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)

root.mainloop()
#-----------------------------------------------------------------------
import tkinter as tk

window = tk.Tk()
window.bind("<Motion>", print)
window.mainloop()

# widget.config(fg="red", bg="blue", font = "Arial") # Ability to change the widget

# widget["fg"] = "red"

#-----------------------------------------------------------------------
# window.geometry(500 x 500)
# window.title("My app")

tk.Label # Text anywhere on the screen
tk.Entry
label = tk.label = tk.label(window, text="Hi")
label["font"] = ("Arial", 16, "bold")
#-----------------------------------------------------------------------

# stringvar()
# IntVar()
# DoubleVar()
# BoolenaVar()
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------