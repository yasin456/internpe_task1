import time
import tkinter as tk

class DigitalClock(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(self, font=("Arial", 40))
        self.label.pack()

        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.config(text=current_time)

        # Update the time every second
        self.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Digital Clock")

    clock = DigitalClock(root)
    clock.pack()

    root.mainloop()
