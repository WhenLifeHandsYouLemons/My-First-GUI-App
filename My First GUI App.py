import tkinter as tk

class App():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry("3000x2000")
        self.window.title("My First GUI App")
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)
        self.label = tk.Label(self.window, text="Welcome To My First GUI App", font=("Arial", 48))
        self.label.place(x=20, y=20)

root = tk.Tk()
root.withdraw()

window1 = App(root)

root.mainloop()