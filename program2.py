import tkinter as tk

class InfoApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("User Info")
        self.window.geometry("350x200")

        self.info_label = tk.Label(self.window, text="", font=("Arial", 12), justify="left")
        self.info_label.pack(pady=20)

        self.show_button = tk.Button(self.window, text="Show Info", command=self.show_info)
        self.show_button.pack(pady=5)

        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy)
        self.quit_button.pack(pady=5)

    def show_info(self):
        name = "Ray McMillin"
        address = "618 Oak Drive\nRoseau, MN 56751"
        self.info_label.config(text=f"Name: {name}\nAddress:\n{address}")

    def run(self):
        self.window.mainloop()

app = InfoApp()
app.run()
