from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x600+0+0")
        self.root.title("face Recognition system")

        title_lbl=Label(self.root,text="HELP DESK",font=("Helvetica",34,"bold"),bg="white",fg="blue",)
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img_top=Image.open(r"C:\Users\Hp\Desktop\Face_recognizationsystem\photos\help2.jpg")
        img_top=img_top.resize((1350,638),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=55,width=1350,height=638)

        dev_label=Label(f_lbl,text="Email: bhavyabaheti@gmail.com",font=("Helvetica",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=30,y=545)









if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()