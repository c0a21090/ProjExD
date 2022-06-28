import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとんゲーム")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    root.mainloop()
    label = tk.Label(root,font=("Times New Roman",80))
    label.pack()