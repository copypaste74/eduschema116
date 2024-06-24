import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter Test")

tk.Label(root, text="Hello, Tkinter!").pack(pady=20)
tk.Button(root, text="Click Me", command=lambda: print("Button Clicked")).pack(pady=20)

root.mainloop()
