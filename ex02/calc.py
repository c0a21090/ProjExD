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

    if num == "?":       #?ボタンを押したら(ちなみにこのボタンは未完成)
        eqn = entry.get()   
        res = eval(eqn)
        entry.delete(0,tk.END)
        ans = input("答えは何?")   #答えを入力する
        entry.insert(tk.END,ans)
        if ans == res:         #入力した値と答えを比べる
            entry.insert(tk.END,"正解")   #等しければ正解と表示
        else:
            entry.insert(tk.END,"不正解")  #違えば不正解と表示
    if num == "**":          #**ボタンを押したら
        eqn = entry.get()   #計算が取得され、累乗される
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    if num == "c":          #cボタンを押すと表示されている値が削除される
        entry.delete(0,tk.END)

    if num == "×":    #×ボタンを押したら
        eqn = entry.get()    #式が取得され、掛け算がされる
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    if num == "/":     #/ボタンを押したら
        eqn = entry.get()      #式が取得され、割り算がされる
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    if num == "押すな":     #押すなボタンを押したら
        entry.delete(0,tk.END)    #値が削除され、ばーかと表示される
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