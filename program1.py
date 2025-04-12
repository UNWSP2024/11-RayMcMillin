#Ray McMillin, 4/11/25, Favorite Saying GUI

import tkinter as tk

class MotivationApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Motivation")
        self.window.geometry("300x100")

        self.label = tk.Label(self.window, text="Slow and steady wins the race!", font=("Arial", 12))
        self.label.pack(pady=20)

    def run(self):
        self.window.mainloop()

app = MotivationApp()
app.run()
