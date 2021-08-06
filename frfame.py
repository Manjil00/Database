from tkinter import *
root=Tk()
root.title("lkjbvsdhB")
root.iconbitmap("")
root.geometry("800x600")
def new():
    def newwindow():
        root2=Toplevel()
        lbl=Label(root2,text="nayawindow").grid(row=0,column=0)
        root2.mainloop()
    fr=LabelFrame(root,text="new frame").grid(row=0,column=0)
    l=Label(fr,text="label inside").grid(row=1,column=0)
    btn1=Button(fr,text="new window",command=newwindow).grid(row=2,column=0)
btn=Button(root,text="qwert", command=new).grid(row=0,column=0)

mainloop()
