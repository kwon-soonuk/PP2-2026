import tkinter as tk

window = tk.Tk()
window.title("hello 권순욱")
window.geometry("400x200")
label = tk.Label(window, text="Hello GUI!")
label.pack()

window.mainloop()