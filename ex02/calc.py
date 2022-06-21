import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    button = event.widget
    num = button["text"]
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
    #tkm.showinfo("",f"{i}のボタンがクリックされました")
        entry.insert(tk.END,num)


    if num == "?":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        ans = input("答えは何?")
        entry.insert(tk.END,ans)
        if ans == res:
            entry.insert(tk.END,"正解")
        else:
            entry.insert(tk.END,"不正解")
    if num == "**":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    if num == "c":
        entry.delete(0,tk.END)

    if num == "×":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    if num == "/":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    if num == "押すな":
        entry.delete(0,tk.END)
        entry.insert(tk.END,"ばーか")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x600")
    root.title("電卓")
    entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=5)
    r=1;c=0
    for i,num in enumerate([9,8,7,6,5,4,3,2,1,0,"+","=","c","*","/","?","**","押すな"]):
        button = tk.Button(root,text=num,width=4,height=1,
                        font=("Times New Roman",30))
        button.bind("<1>",button_click)
        button.grid(row=r,column=c)
        c += 1
        if (i+1)%3==0:
            r += 1
            c = 0
        #button.pack()
    root.mainloop()